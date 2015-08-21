# -*- coding: utf-8 -*-
import re

STOMACH_CANCER_ICDS = ['C16.1', 'C16.2', 'C16.3', 'C16.4', 'C16.5', 'C16.6', 'C16.8', 'C16.9']

class StomachCancerStager(object):

    STOMACH_CANCER_TS = ['Tis', 'T1', 'T2', 'T3', 'T4', 'T4a', 'T4b']
    STOMACH_CANCER_NS = ['N0', 'N1', 'N2']
    STOMACH_CANCER_MS = ['M0', 'M1']

    def __init__(self, icd, t, n, m):
        self.valid = False
        self.validation_message = 'No message set'
        self.stage = None
        self.icd = icd
        self.t = t
        self. n = n
        self.m = m
        self.validate_tnm()
        self.staging()

    def staging(self):

        TNM = self.t + self.n + self.m

        if re.match('(TisN0M0)', TNM, re.IGNORECASE):
            self.stage = '0'
        elif re.match('T1N0M0', TNM, re.IGNORECASE):
            self.stage = 'IA'
        elif re.match('(T2N0M0|T1N1M0)', TNM, re.IGNORECASE):
            self.stage = 'IB'
        elif re.match('(T3N0M0|T2N1M0|T1N2M0)', TNM, re.IGNORECASE):
            self.stage = 'IIA'
        elif re.match('(T4aN0M0|T3N1M0|T2N2M0|T1N3M0)', TNM, re.IGNORECASE):
            self.stage = 'IIB'
        elif re.match('(T4aN1M0|T3N2M0|T2N3M0)', TNM, re.IGNORECASE):
            self.stage = 'IIIA'
        elif re.match('(T4bN0M0|T4bN1M0|T4aN2M0|T3N3M0)', TNM, re.IGNORECASE):
            self.stage = 'IIIB'
        elif re.match('(T4bN2M0|T4bN3M0|T4aN3M0)', TNM, re.IGNORECASE):
            self.stage = 'IIIC'
        elif re.match('.+M1', TNM, re.IGNORECASE):
            self.stage = 'IV'
        else:
            self.stage = None

    def validate_tnm(self):
        if self.t not in self.STOMACH_CANCER_TS:
            self.valid = False
            self.validation_message = 'Invalid T: ' + self.t + ' for ICD: ' + self.icd + '. Valid Ts are ' + str(self.STOMACH_CANCER_TS)
        elif self.n not in self.STOMACH_CANCER_NS:
            self.valid = False
            self.validation_message = 'Invalid N: ' + self.n + ' for ICD: ' + self.icd + '. Valid Ns are ' + str(self.STOMACH_CANCER_NS)
        elif self.m not in self.STOMACH_CANCER_MS:
            self.valid = False
            self.validation_message = 'Invalid M: ' + self.m + ' for ICD: ' + self.icd + '. Valid Ms are ' + str(self.STOMACH_CANCER_MS)
        else:
            self.valid = True
            self.validation_message = 'Valid Stomach TNM'


