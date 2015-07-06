# -*- coding: utf-8 -*-
import re

PROSTATE_CANCER_ICDS = ['C61', 'C61.9']

class ProstateCancerStager(object):

    PROSTATE_CANCER_TS = ['T1', 'T1a', 'T1b', 'T1c', 'T2', 'T2a', 'T2b', 'T2c', 'T3', 'T3a', 'T3b', 'T4']
    PROSTATE_CANCER_NS = ['N0', 'N1']
    PROSTATE_CANCER_MS = ['M0', 'M1']
    PROSTATE_CANCER_PSA = ['P1', 'P2', 'P3', 'PX']
    PROSTATE_CANCER_GLEASON = ['G1', 'G2', 'G3', 'GX']

    def __init__(self, icd, t, n, m, psa, gleason):
        self.valid = False
        self.validation_message = 'No message set'
        self.stage = None
        self.icd = icd
        self.t = t
        self. n = n
        self.m = m
        self.psa = self.psa_calc(psa)
        self.gleason = self.gleason_calc(gleason)
        self.validate_tnm_psa_gleason()
        self.staging()

    def staging(self):

        TNMPG = self.t + self.n + self.m + self.psa + self.gleason

        if re.match('(T1aN0M0P1G1|T1bN0M0P1G1|T1cN0M0P1G1|T2aN0M0P1G1|T1N0M0PXGX|T1aN0M0PXGX|T1bN0M0PXGX|T1cN0M0PXGX|T2N0M0PXGX|T2aN0M0PXGX)', TNMPG, re.IGNORECASE):
            self.stage = 'I'
        elif re.match('(T1aN0M0P1G2|T1bN0M0P1G2|T1cN0M0P1G2|T1aN0M0P2G2|T1bN0M0P2G2|T1cN0M0P2G2|T1aN0M0P2G1|T1bN0M0P2G1|T1cN0M0P2G1|T2aN0M0P1G1|T2aN0M0P1G2|T2aN0M0P2G1|T2aN0M0P2G2|T2bN0M0P1G1|T2bN0M0P1G2|T2bN0M0P2G1|T2bN0M0P2G2|T2bN0M0PXGX)', TNMPG, re.IGNORECASE):
            self.stage = 'IIA'
        elif re.match('(T2cN0M0.+|T1N0M0P3.+|T1.+N0M0P3.+|T2N0M0P3.+|T1N0M0.+G3|T1.+N0M0.+G3|T2N0M0.+G3)', TNMPG, re.IGNORECASE):
            self.stage = 'IIB'
        elif re.match('(T3aN0M0.+|T3bN0M0.+)', TNMPG, re.IGNORECASE):
            self.stage = 'III'
        elif re.match('(T4N0M0.+|.+N1M0.+|.+M1.+)', TNMPG, re.IGNORECASE):
            self.stage = 'IV'
        else:
            self.valid = False
            self.validation_message = 'Impossible to calculate stage for ' + self.t + ' ' + self.n + ' ' + self.m
            self.stage = None

    def validate_tnm_psa_gleason(self):
        if self.t not in self.PROSTATE_CANCER_TS:
            self.valid = False
            self.validation_message = 'Invalid T: ' + self.t + ' for ICD: ' + self.icd + '. Valid Ts are ' + str(self.PROSTATE_CANCER_TS)

        if self.n not in self.PROSTATE_CANCER_NS:
            self.valid = False
            self.validation_message = 'Invalid N: ' + self.n + ' for ICD: ' + self.icd + '. Valid Ns are ' + str(self.PROSTATE_CANCER_NS)

        if self.m not in self.PROSTATE_CANCER_MS:
            self.valid = False
            self.validation_message = 'Invalid M: ' + self.m + ' for ICD: ' + self.icd + '. Valid Ms are ' + str(self.PROSTATE_CANCER_MS)

        if self.psa not in self.PROSTATE_CANCER_PSA:
            self.valid = False
            self.validation_message = 'Invalid PSA: ' + self.psa + ' for ICD: ' + self.icd + '. Valid PSA are ' + str(self.PROSTATE_CANCER_PSA)

        if self.gleason not in self.PROSTATE_CANCER_GLEASON:
            self.valid = False
            self.validation_message = 'Invalid GLEASON: ' + self.gleason + ' for ICD: ' + self.icd + '. Valid GLEASON are ' + str(self.PROSTATE_CANCER_GLEASON)
        else:
            self.valid = True
            self.validation_message = 'Valid Prostate TNM, Gleason and PSA'

    def psa_calc(self, psa):
        if psa == 'x' or psa =='X':
            return 'PX'
        if psa < 10:
            return 'P1'
        elif psa >= 10 and psa < 20:
            return 'P2'
        elif psa >= 20:
            return 'P3'

    def gleason_calc(self, gleason):
        if gleason == 'x' or gleason == 'X':
            return 'GX'
        if gleason <= 6:
            return 'G1'
        elif gleason <= 7:
            return 'G2'
        elif gleason >= 8:
            return 'G3'