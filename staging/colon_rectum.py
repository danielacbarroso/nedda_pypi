# -*- coding: utf-8 -*-
import re

COLON_CANCER_ICDS = ['C18.0', 'C18.2', 'C18.3', 'C18.4', 'C18.5', 'C18.6', 'C18.7', 'C18.8', 'C18.9', 'C19.9', 'C20.9']

class ColonRectumStager(object):

    COLON_CANCER_TS = ['Tis', 'T1', 'T2', 'T3', 'T4a', 'T4b', 'T1-T2', 'T2-T3', 'T3-T4a']
    COLON_CANCER_NS = ['N0', 'N1', 'N1c', 'N2a', 'N2b', 'Ni-N2']
    COLON_CANCER_MS = ['M0', 'M1a', 'M1b']
    COLON_CANCER_DUKES = ['A', 'B', 'C', None]
    
    def __init__(self, icd, t, n, m, dukes):
        self.valid = False
        self.validation_message = 'No message set'
        self.stage = None
        self.icd = icd
        self.t = t
        self. n = n
        self.m = m
        self.dukes = dukes
        self.validate_tnm_dukes()
        self.staging()

    def staging(self):    
    
        TNMD = self.t + self.n + self.m + self.dukes
        
        if re.match('TisN0M0', TNMD, re.IGNORECASE):
            self.stage = '0'    
        elif re.match('(T1N0M0A|T2N0M0A)', TNMD, re.IGNORECASE):
            self.stage = 'I'
        elif re.match('T3N0M0B', TNMD, re.IGNORECASE):
            self.stage = 'IIA'
        elif re.match('T4aN0M0B', TNMD, re.IGNORECASE):
            self.stage = 'IIB'
        elif re.match('T4bN0M0B', TNMD, re.IGNORECASE):
            self.stage = 'IIC'
        elif re.match('(T1-T2N1M0C|T1-T2N1cM0C|T1N2aM0C)', TNMD, re.IGNORECASE):
            self.stage = 'IIIA'
        elif re.match('(T3-T4aN1M0C|T3-T4aN1cM0C|T2-T3N2aM0C|T1-T2N2bM0C)', TNMD, re.IGNORECASE):
            self.stage = 'IIIB'
        elif re.match('T4aN2aM0C|T3-T4aN2bM0C|T4bN1-N2M0C', TNMD, re.IGNORECASE):
            self.stage = 'IIIC'
        elif re.match('.+M1a', TNMD, re.IGNORECASE):
            self.stage = 'IVA'
        elif re.match('.+M1B', TNMD, re.IGNORECASE):
            self.stage = 'IVB'
        else:
            self.stage = None

    def validate_tnm_dukes(self):

            if self.t not in self.COLON_CANCER_TS:
                self.valid = False
                self.validation_message = 'Invalid T: ' + self.t + ' for ICD: ' + self.selficd + '. Valid Ts are ' + str(self.COLON_CANCER_TS)
    
            if self.n not in self.COLON_CANCER_NS:
                self.valid = False
                self.validation_message = 'Invalid N: ' + self.n + ' for ICD: ' + self.icd + '. Valid Ns are ' + str(self.COLON_CANCER_NS)
    
            if self.m not in self.COLON_CANCER_MS:
                self.valid = False
                self.validation_message = 'Invalid M: ' + self.m + ' for ICD: ' + self.icd + '. Valid Ms are ' + str(self.COLON_CANCER_MS)
    
            if self.dukes not in self.COLON_CANCER_DUKES:
                self.valid = False
                self.validation_message = 'Invalid Dukes: ' + self.dukes + 'for ICD' + self.icd + '. Valid Dukes are' + str(self.COLON_CANCER_DUKES)
            else:
                self.valid = True
                self.validation_message = 'Valid Colon/Rectum TNM'
