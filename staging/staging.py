# -*- coding: utf-8 -*-
import os
import csv

STAGES = list()

with open(os.path.dirname(os.path.abspath(__file__)) + '/data/staging/stages.csv', 'rt') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        icds_set = row[0].split('-')
        STAGES.append({
            'icd': icds_set,
            't': row[1],
            'n': row[2],
            'm': row[3],
            'dukes': row[4],
            'stage': row[5]
            })

class GenericStager(object):
    
    t_set = set()
    n_set = set()
    m_set = set()
    stages_dict = dict()
    icd_set = set()

    def __init__(self, icd, t, n, m):
        self.valid = True
        self.validation_message = 'No message set'
        self.stage = None
        for i in icd:
            i = icd.split('.')[0].upper() # considers only the first part o ICD
            self.icd_set.add(i)
        self.t = t
        self. n = n
        self.m = m

        for item in STAGES:
            for icd in item['icd']:
                if icd in self.icd_set:
                    self.t_set.add(item['t'])
                    self.n_set.add(item['n'])
                    self.m_set.add(item['m'])
                    self.stages_dict[item['t'] + item['n'] + item['m']] = item['stage']

        self.validate_tnm()
        self.staging()

    def staging(self):
        TNM = self.t + self.n + self.m
        try:
            self.stage = self.stages_dict[TNM]
        except KeyError:
            self.stage = None

    def validate_tnm(self):
        if self.t not in self.t_set:
            self.valid = False
            self.validation_message = 'Invalid T: ' + self.t + ' for ICD: ' + self.icd + '. Valid Ts are ' + str(self.t_set)
        if self.n not in self.n_set:
            self.valid = False
            self.validation_message = self.validation_message + '\nInvalid N: ' + self.n + ' for ICD: ' + self.icd + '. Valid Ns are ' + str(self.n_set)
        if self.m not in self.m_set:
            self.valid = False
            self.validation_message = self.validation_message + '\nInvalid M: ' + self.m + ' for ICD: ' + self.icd + '. Valid Ms are ' + str(self.m_set)
        if self.valid:
            self.validation_message = 'Valid TNM'

class ColonRectumStager(GenericStager):

    dukes_set = set()

def tnm_stage(icd, t, n, m, dukes=None, psa=None, gleason=None):
    icd = icd.strip()
    stager = GenericStager(icd, t, n, m)
    return stager.stage