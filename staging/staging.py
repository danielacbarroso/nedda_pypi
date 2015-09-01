# -*- coding: utf-8 -*-
import os
import csv
import re

STAGES = list()
# TUMOR_t = list()
# NODES_n = list()
# METASTASES_m = list()
NEOPLASMS_c = list()
# DUKES_dukes = list()
# PSA_psa = list()
# GLEASON_gleason = list()
vetor = []

with open(os.path.dirname(os.path.abspath(__file__)) + '/data/staging/icdname.csv', 'rt') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvreader.next()
    for row in csvreader:
        NEOPLASMS_c.append({
            'neoplasms': row[0],
            'ICD': row[1]
            })

with open(os.path.dirname(os.path.abspath(__file__)) + '/data/staging/stages.csv', 'rt') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvreader.next()
    for row in csvreader:
        STAGES.append({
            'icd': row[0],
            't': row[1],
            'n': row[2],
            'm': row[3],
            'dukes': row[4],
            'stage': row[5],
            'psa': row[6],
            'gleason': row[7],
            'carcinosarcoma': row[8],
            'neoplasms': row[9]
            })


class GenericStager(object):
    
    _t_set = set()
    _n_set = set()
    _m_set = set()
    dukes_set = set()
    psa_set = set()
    gleason_set = set()
    neoplasms_set = set()
    carcinosarcoma_set = set()
    stages_dict = dict()

    def __init__(self, icd, t=None, n=None, m=None, dukes=None, psa=None, gleason=None, carcinosarcoma=None,
                 neoplasms=None):
        self.valid = True
        self.validation_message = 'No message set'
        self.stage = None
        self.icd = icd#icd.split('.')[0].upper() # considers only the first part o ICD
        self.t = t
        self.n = n
        self.m = m
        self.dukes = dukes
        self.psa = psa
        self.gleason = gleason
        self.carcinosarcoma = carcinosarcoma
        self.neoplasms = neoplasms

        if self._t_set.__len__() > 0:
            self._t_set = set()
        if self._n_set.__len__() > 0:
            self._n_set = set()
        if self._m_set.__len__() > 0:
            self._m_set = set()

        for item in STAGES:

            if self.icd == item['icd']:

                 if item['t'] is None:
                    self._t_set.add(STAGES[item['icd']])
                 else:
                    self._t_set.add(item['t'])

                 self._n_set.add(item['n'])
                 self._m_set.add(item['m'])

                 if item['dukes'] == '':
                     self.dukes_set.add('-')
                 else:
                     self.dukes_set.add(item['dukes'])

                 if item['psa'] == '':
                     self.psa_set.add('-')
                 else:
                     self.psa_set.add(item['psa'])

                 if item['gleason'] == '':
                     self.gleason_set.add('-')
                 else:
                     self.gleason_set.add(item['gleason'])

                 self.carcinosarcoma_set.add(item['carcinosarcoma'])
                 self.neoplasms_set.add(item['neoplasms'])
                 self.stages_dict[item['t'] + item['n'] + item['m'] + item['dukes'] + item['psa'] + item['gleason']
                                  + item['carcinosarcoma']] = item['stage']


        if self.t is not None:
            self.validate_tnm()
            self.staging()

    def __del__(self):
        self._t_set=None

    def get_t_set(self):
        return self._t_set

    def get_t_list(self):
        ordered_t_list = sorted(self.get_t_set())

        #opcao usada para colocar o Tis como primeiro, caso exista
        try:
            ordered_t_list.remove('Tis')
            #del ordered_t_list[ordered_t_list.index(tis)]
            ordered_t_list = ['Tis'] + ordered_t_list
            return ordered_t_list
        except ValueError:
            return ordered_t_list


    def get_n_set(self):
        return self._n_set
    def get_n_list(self):
        return sorted(self.get_n_set())

    def get_m_set(self):
        return self._m_set
    def get_m_list(self):
        return sorted(self.get_m_set())


    def staging(self):
        if self.t is None:
            TNM = ""
        else:
            TNM = self.t

        if self.n is None:
            TNM = TNM + ""
        else:
            TNM = TNM + self.n

        if self.m is None:
            TNM = TNM + ""
        else:
            TNM = TNM + self.m

        if self.dukes is None:
            TNM = TNM + ""
        else:
            TNM = TNM + self.dukes

        if self.psa is None:
            TNM = TNM + ""
        else:
            TNM = TNM + self.psa

        if self.gleason is None:
            TNM = TNM + ""
        else:
            TNM = TNM + self.gleason

        if self.carcinosarcoma is None:
            TNM = TNM + ""
        else:
            TNM = TNM + self.carcinosarcoma

        if self.neoplasms is None:
            TNM = TNM + ""
        else:
            TNM = TNM + self.neoplasms

        try:
            self.stage = self.stages_dict[TNM]
        except KeyError:
            self.stage = None

    def validate_tnm(self):
        if self.t not in self._t_set:
            self.valid = False
            self.validation_message = 'Invalid T: ' + self.t + ' for ICD: ' + str(self.icd) + '. Valid Ts are ' + str(self._t_set)
        if self.n not in self._n_set:
            self.valid = False
            self.validation_message = self.validation_message + '\nInvalid N: ' + str(self.n) + ' for ICD: ' + str(self.icd) + '. Valid Ns are ' + str(self._n_set)
        if self.m not in self._m_set:
            self.valid = False
            self.validation_message = self.validation_message + '\nInvalid M: ' + str(self.m) + ' for ICD: ' + str(self.icd) + '. Valid Ms are ' + str(self._m_set)
        if self.valid:
            self.validation_message = 'Valid TNM'

def tnm_stage(icd, t=None, n=None, m=None, dukes=None, psa=None, gleason=None, carcinosarcoma=None, neoplasms=None):

    icd = icd.split('-')[0].strip()

    stager = GenericStager(icd, t, n, m, dukes, psa, gleason, carcinosarcoma, neoplasms)
    return stager.stage