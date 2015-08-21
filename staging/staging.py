# -*- coding: utf-8 -*-
import os
import csv
import re

STAGES = list()

with open(os.path.dirname(os.path.abspath(__file__)) + '/data/staging/stages.csv', 'rt') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        STAGES.append({
            'icd': row[0],
            't': row[1],
            'n': row[2],
            'm': row[3],
            'dukes': row[4],
            'stage': row[5],
            'psa': row[6],
            'gleason': row[7]
            })

class GenericStager(object):
    
    t_set = set()
    n_set = set()
    m_set = set()
    dukes_set = set()
    psa_set = set()
    gleason_set = set()
    stages_dict = dict()

    def __init__(self, icd, t, n, m, dukes, psa, gleason):
        self.valid = True
        self.validation_message = 'No message set'
        self.stage = None
        self.icd = icd.split('.')[0].upper() # considers only the first part o ICD
        self.t = t
        self. n = n
        self.m = m
        self.dukes = dukes
        self.psa = psa
        self.gleason = gleason

        for item in STAGES:
            if self.icd == item['icd']:
                self.t_set.add(item['t'])
                self.n_set.add(item['n'])
                self.m_set.add(item['m'])
                self.dukes_set.add(item['dukes'])
                self.psa_set.add(item['psa'])
                self.gleason_set.add(item['gleason'])
                self.stages_dict[item['t'] + item['n'] + item['m'] + item['dukes'] + item['psa'] + item['gleason']] = item['stage']

        self.validate_tnm()
        self.staging()

    def staging(self):
        if self.dukes is None:
            TNM = self.t + self.n + self.m + ""
        else:
            TNM = self.t + self.n + self.m + self.dukes

        try:
            self.stage = self.stages_dict[TNM]
        except KeyError:
            self.stage = None

    def validate_tnm(self):
        if self.t not in self.t_set:
            self.valid = False
            self.validation_message = 'Invalid T: ' + self.t + ' for ICD: ' + str(self.icd) + '. Valid Ts are ' + str(self.t_set)
        if self.n not in self.n_set:
            self.valid = False
            self.validation_message = self.validation_message + '\nInvalid N: ' + str(self.n) + ' for ICD: ' + str(self.icd) + '. Valid Ns are ' + str(self.n_set)
        if self.m not in self.m_set:
            self.valid = False
            self.validation_message = self.validation_message + '\nInvalid M: ' + str(self.m) + ' for ICD: ' + str(self.icd) + '. Valid Ms are ' + str(self.m_set)
        if self.valid:
            self.validation_message = 'Valid TNM'

def tnm_stage(icd, t, n, m, dukes=None, psa=None, gleason=None):
    icd = icd.strip()
    stager = GenericStager(icd, t, n, m, dukes, psa, gleason)
    return stager.stage