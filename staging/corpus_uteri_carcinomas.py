# -*- coding: utf-8 -*-
__author__ = 'sandra'

import re

CORPUS_UTERI_CANCER_ICDS = ['C54.0', 'C54.1', 'C54.2', 'C54.3', 'C54.8', 'C54.9', 'C55.9']

class CorpusUteriCarcinomaStager(object):

    CORPUS_UTERI_CANCER_TS = ['Tis', 'T1', 'T1a', 'T1b', 'T2', 'T3', 'T3a', 'T3b', 'T4']
    CORPUS_UTERI_CANCER_NS = ['N0', 'N1', 'N2']
    CORPUS_UTERI_CANCER_MS = ['M0', 'M1']

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
        elif re.match('T1bN0M0', TNM, re.IGNORECASE):
            self.stage = 'IB'
        elif re.match('T2N0M0', TNM, re.IGNORECASE):
            self.stage = 'II'
        elif re.match('T3N0M0', TNM, re.IGNORECASE):
            self.stage = 'III'
        elif re.match('T3aN0M0', TNM, re.IGNORECASE):
            self.stage = 'IIIA'
        elif re.match('T3bN0M0', TNM, re.IGNORECASE):
            self.stage = 'IIIB'
        elif re.match('(T1N1M0|T2N1M0|T3N1M0)', TNM, re.IGNORECASE):
            self.stage = 'IIIC1'
        elif re.match('(T1N2M0|T2N2M0|T3N2M0)', TNM, re.IGNORECASE):
            self.stage = 'IIIC2'
        elif re.match('T4.+M0', TNM, re.IGNORECASE):
            self.stage = 'IVA'
        elif re.match('.+M1', TNM, re.IGNORECASE):
            self.stage = 'IVB'
        else:
            self.stage = None


    def validate_tnm(self):
        if self.t not in  self.CORPUS_UTERI_CANCER_TS:
            self.valid = False
            self.validation_message = 'Invalid T: ' + self.t + ' for ICD: ' + self.icd + '. Valid Ts are ' + str(self.CORPUS_UTERI_CANCER_TS)
        elif self.n not in self.CORPUS_UTERI_CANCER_NS:
            self.valid = False
            self.validation_message = 'Invalid N: ' + self.n + ' for ICD: ' + self.icd + '. Valid Ns are ' + str(self.CORPUS_UTERI_CANCER_NS)

        elif self.m not in self.CORPUS_UTERI_CANCER_MS:
            self.valid = False
            self.validation_message =  'Invalid M: ' + self.t + ' for ICD: ' + self.icd + '. Valid Ms are ' + str(self.CORPUS_UTERI_CANCER_MS)
        else:
            self.valid = True
            self.validation_message = 'Valid Corpus Uteri Carcinomas TNM'