# -*- coding: utf-8 -*-
import os
import csv

BREAST_CANCER_ICDS = ['C50', 'C50.0', 'C50.1', 'C50.2', 'C50.3', 'C50.4', 'C50.5', 'C50.6', 'C50.7', 'C50.8', 'C50.9']

class BreastCancerStager(object):

    BREAST_CANCER_TS = set()
    BREAST_CANCER_NS = set()
    BREAST_CANCER_MS = set()
    BREAST_STAGING_DICT = dict()

    with open(os.path.dirname(os.path.abspath(__file__)) + '/data/staging/breast.csv', 'rt') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            t = row[0]
            n = row[1]
            m = row[2]
            stage = row[3]
            BREAST_CANCER_TS.add(t)
            BREAST_CANCER_NS.add(n)
            BREAST_CANCER_MS.add(m)
            BREAST_STAGING_DICT[t+n+m] = stage

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

        try:
            self.stage = self.BREAST_STAGING_DICT[TNM]
        except KeyError:
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