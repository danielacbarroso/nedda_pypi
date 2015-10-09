# -*- coding: utf-8 -*-
import os
import csv

STAGES = list()

with open(os.path.dirname(os.path.abspath(__file__)) + '/data/stages.csv', 'rt') as csvfile:
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
    
    def __init__(self, icd, t=None, n=None, m=None, dukes=None, psa=None, gleason=None, carcinosarcoma=None,
                 neoplasms=None):
        self._t_set = set()
        self._n_set = set()
        self._m_set = set()
        self._dukes_set = set()
        self._psa_set = set()
        self._gleason_set = set()
        self.neoplasms_set = set()
        self.carcinosarcoma_set = set()
        self.stages_dict = dict()
        self.valid = True
        self.validation_message = 'No message set'
        self.stage = None
        self.icd = icd #icd.split('.')[0].upper() # considers only the first part o ICD
        self.t = t
        self.n = n
        self.m = m
        self.dukes = dukes
        self.psa = psa
        self.gleason = gleason
        self.carcinosarcoma = carcinosarcoma
        self.neoplasms = neoplasms

        for item in STAGES:

            if self.icd == item['icd']:

                 if item['t'] is None:
                    self._t_set.add(STAGES[item['icd']])
                 else:
                    self._t_set.add(item['t'])

                 self._n_set.add(item['n'])
                 self._m_set.add(item['m'])

                 if item['dukes'] == '':
                     self._dukes_set.add('-')
                 else:
                     self._dukes_set.add(item['dukes'])

                 if item['psa'] == '':
                     self._psa_set.add('-')
                 else:
                     self._psa_set.add(item['psa'])

                 if item['gleason'] == '':
                     self._gleason_set.add('-')
                 else:
                     self._gleason_set.add(item['gleason'])

                 self.carcinosarcoma_set.add(item['carcinosarcoma'])
                 self.neoplasms_set.add(item['neoplasms'])
                 self.stages_dict[item['t'] + item['n'] + item['m'] + item['dukes'] + item['psa'] + item['gleason']
                                  + item['carcinosarcoma']] = item['stage']

        if self.t is not None:
            self.validate_tnm()
            self.staging()

    def get_t_set(self):
        return self._t_set

    def get_t_list(self):

        ordered_t_list = sorted(self.get_t_set())
        # This option is to put 'Tis' first, in case it exists
        try:
            ordered_t_list.remove('Tis')
            ordered_t_list = ['Tis'] + ordered_t_list
            return ordered_t_list
        except ValueError:
            return ordered_t_list

    def get_n_list(self):
        return sorted(self._n_set)

    def get_m_list(self):
        return sorted(self._m_set)

    def get_dukes_list(self):
        return sorted(list(self._dukes_set))

    def get_psa_list(self):
        return sorted(list(self._psa_set))

    def get_gleason_list(self):
        return sorted(list(self._gleason_set))

    def staging(self):

        TNM = ''

        if self.t is not None:
            TNM = self.t

        if self.n is not None:
            TNM += self.n

        if self.m is not None:
            TNM += self.m

        if self.dukes is not None:
            TNM += self.dukes

        if self.psa is not None:
            TNM += self.psa

        if self.gleason is not None:
            TNM += self.gleason

        if self.carcinosarcoma is not None:
            TNM += self.carcinosarcoma

        if self.neoplasms is not None:
            TNM += self.neoplasms

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