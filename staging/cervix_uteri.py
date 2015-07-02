# -*- coding: utf-8 -*-
import re

CERVIX_UTERI_CANCER_ICDS = ['C53.0', 'C53.1', 'C53.8', 'C53.9']

class CervixUteriStager(object):

    CERVIX_UTERI_CANCER_TS = ['Tis', 'T1', 'T1a', 'T1a1', 'T1a2', 'T1b', 'T1b1', 'T1b2', 'T2', 'T2a', 'T2a1', 'T2a2', 'T2b', 'T3', 'T3a', 'T3b', 'T1-3', 'T4']
    CERVIX_UTERI_CANCER_NS = ['N0', 'N1']
    CERVIX_UTERI_CANCER_MS = ['M0', 'M1']

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
            self.stage = 'I'
        elif re.match('T1aN0M0', TNM, re.IGNORECASE):
            self.stage = 'IA'
        elif re.match('T1a1N0M0', TNM, re.IGNORECASE):
            self.stage = 'IA1'
        elif re.match('T1a2N0M0', TNM, re.IGNORECASE):
            self.stage = 'IA2'
        elif re.match('T1bN0M0', TNM, re.IGNORECASE):
            self.stage = 'IB'
        elif re.match('T1b1N0M0', TNM, re.IGNORECASE):
            self.stage = 'IB1'
        elif re.match('T1b2N0M0', TNM, re.IGNORECASE):
            self.stage = 'IB2'
        elif re.match('T2N0M0', TNM, re.IGNORECASE):
            self.stage = 'II'
        elif re.match('T2aN0M0', TNM, re.IGNORECASE):
            self.stage = 'IIA'
        elif re.match('T2a2N0M0', TNM, re.IGNORECASE):
            self.stage = 'IIA2'
        elif re.match('T2bN0M0', TNM, re.IGNORECASE):
            self.stage = 'IIB'
        elif re.match('T3N0M0', TNM, re.IGNORECASE):
            self.stage = 'III'
        elif re.match('T3aN0M0', TNM, re.IGNORECASE):
            self.stage = 'IIIA'
        elif re.match('(T3b.+M0|T1-3N1M0)', TNM, re.IGNORECASE):
            self.stage = 'IIIB'
        elif re.match('T4.+M0', TNM, re.IGNORECASE):
            self.stage = 'IVA'
        elif re.match('.+M1', TNM, re.IGNORECASE):
            self.stage = 'IVB'
        else:
            self.stage = None


    def validate_tnm(self):
        if self.t not in  self.CERVIX_UTERI_CANCER_TS:
            self.valid = False
            self.validation_message = 'Invalid T: ' + self.t + ' for ICD: ' + self.icd + '. Valid Ts are ' + str(self.CERVIX_UTERI_CANCER_TS)
        elif self.n not in self.CERVIX_UTERI_CANCER_NS:
            self.valid = False
            self.validation_message = 'Invalid N: ' + self.n + ' for ICD: ' + self.icd + '. Valid Ns are ' + str(self.CERVIX_UTERI_CANCER_NS)

        elif self.m not in self.CERVIX_UTERI_CANCER_MS:
            self.valid = False
            self.validation_message =  'Invalid M: ' + self.t + ' for ICD: ' + self.icd + '. Valid Ms are ' + str(self.CERVIX_UTERI_CANCER_MS)
        else:
            self.valid = True
            self.validation_message = 'Valid Cervix Uteri TNM'