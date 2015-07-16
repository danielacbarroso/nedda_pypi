# -*- coding: utf-8 -*-
import re

LUNG_CANCER_ICDS = ['C34', 'C34.0', 'C34.1', 'C34.2', 'C34.3', 'C34.8', 'C34.9']

class LungCancerStager(object):

    LUNG_CANCER_TS = ['Tis', 'T1a', 'T1b', 'T2a', 'T2b', 'T3', 'T4']
    LUNG_CANCER_NS = ['N0', 'N1', 'N1mi', 'N2', 'N3']
    LUNG_CANCER_MS = ['M0', 'M1a', 'M1b']

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
        elif re.match('(T1aN0M0|T1bN0M0)', TNM, re.IGNORECASE):
            self.stage = 'IA'
        elif re.match('(T2aN0M0)', TNM, re.IGNORECASE):
            self.stage = 'IB'
        elif re.match('(T2bN0M0|T1aN1M0|T1bN1M0|T2aN1M0)', TNM, re.IGNORECASE):
            self.stage = 'IIA'
        elif re.match('(T2bN1M0|T3N0M0)', TNM, re.IGNORECASE):
            self.stage = 'IIB'
        elif re.match('(T1aN2M0|T1bN2M0|T2aN2M0|T2bN2M0|T3N1M0|T3N2M0|T4N0M0|T4N1M0)', TNM, re.IGNORECASE):
            self.stage = 'IIIA'
        elif re.match('(T1aN3M0|T1bN3M0|T2aN3M0|T2bN3M0|T3N3M0|T4N2M0|T4N3M0)', TNM, re.IGNORECASE):
            self.stage = 'IIIB'
        elif re.match('(.+M1a|.+M1b)', TNM, re.IGNORECASE):
            self.stage = 'IV'
        else:
            self.stage = None

    def validate_tnm(self):
        if self.t not in self.LUNG_CANCER_TS:
            self.valid = False
            self.validation_message = 'Invalid T: ' + self.t + ' for ICD: ' + self.icd + '. Valid Ts are ' + str(self.LUNG_CANCER_TS)
        elif self.n not in self.LUNG_CANCER_NS:
            self.valid = False
            self.validation_message = 'Invalid N: ' + self.n + ' for ICD: ' + self.icd + '. Valid Ns are ' + str(self.LUNG_CANCER_NS)
        elif self.m not in self.LUNG_CANCER_MS:
            self.valid = False
            self.validation_message = 'Invalid M: ' + self.m + ' for ICD: ' + self.icd + '. Valid Ms are ' + str(self.LUNG_CANCER_MS)
        else:
            self.valid = True
            self.validation_message = 'Valid Lung TNM'