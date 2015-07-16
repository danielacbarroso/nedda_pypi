# -*- coding: utf-8 -*-
import re

BREAST_CANCER_ICDS = ['C50', 'C50.0', 'C50.1', 'C50.2', 'C50.3', 'C50.4', 'C50.5', 'C50.6', 'C50.7', 'C50.8', 'C50.9']

class BreastCancerStager(object):

    BREAST_CANCER_TS = ['Tis', 'T0', 'T1', 'T2', 'T3', 'T4']
    BREAST_CANCER_NS = ['N0', 'N1', 'N1mi', 'N2', 'N3']
    BREAST_CANCER_MS = ['M0', 'M1']

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

        if re.match('TisN0M0', TNM, re.IGNORECASE):
            self.stage = '0'
        elif re.match('T1N0M0', TNM, re.IGNORECASE):
            self.stage = 'IA'
        elif re.match('(T0N1miM0|T1N1miM0)', TNM, re.IGNORECASE):
            self.stage = 'IB'
        elif re.match('(T0N1M0|T1N1M0|T2N0M0)', TNM, re.IGNORECASE):
            self.stage = 'IIA'
        elif re.match('(T2N1M0|T3N0M0)', TNM, re.IGNORECASE):
            self.stage = 'IIB'
        elif re.match('(T0N2M0|T1N2M0|T2N2M0|T3N1M0|T3N2M0)', TNM, re.IGNORECASE):
            self.stage = 'IIIA'
        elif re.match('(T4N0M0|T4N1M0|T4N2M0)', TNM, re.IGNORECASE):
            self.stage = 'IIIB'
        elif re.match('.+N3M0', TNM, re.IGNORECASE):
            self.stage = 'IIIC'
        elif re.match('.+M1', TNM, re.IGNORECASE):
            self.stage = 'IV'
        else:
            self.stage = None

    def validate_tnm(self):
        if self.t not in self.BREAST_CANCER_TS:
            self.valid = False
            self.validation_message = 'Invalid T: ' + self.t + ' for ICD: ' + self.icd + '. Valid Ts are ' + str(self.BREAST_CANCER_TS)
        elif self.n not in self.BREAST_CANCER_NS:
            self.valid = False
            self.validation_message = 'Invalid N: ' + self.n + ' for ICD: ' + self.icd + '. Valid Ns are ' + str(self.BREAST_CANCER_NS)
        elif self.m not in self.BREAST_CANCER_MS:
            self.valid = False
            self.validation_message = 'Invalid M: ' + self.m + ' for ICD: ' + self.icd + '. Valid Ms are ' + str(self.BREAST_CANCER_MS)
        else:
            self.valid = True
            self.validation_message = 'Valid Breast TNM'