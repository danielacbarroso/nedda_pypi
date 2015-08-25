# -*- coding: utf-8 -*-
import os
import csv
import re
import numpy

STAGES = list()
TUMOR_t = list()
NODES_n = list()
METASTASES_m = list()
vetor = []


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
            'gleason': row[7],
            'carcinosarcoma': row[8]
            })

        TUMOR_t.append({
            'icd': row[0],
            't': row[1]
            })

        NODES_n.append({
            'icd': row[0],
            'n': row[2]
            })

        METASTASES_m.append({
            'icd': row[0],
            'm': row[3]
            })

class GenericStager(object):
    
    t_set = set()
    n_set = set()
    m_set = set()
    dukes_set = set()
    psa_set = set()
    gleason_set = set()
    carcinosarcoma_set = set()
    stages_dict = dict()

    def __init__(self, icd, t=None, n=None, m=None, dukes=None, psa=None, gleason=None, carcinosarcoma=None):
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
        self.carcinosarcoma = carcinosarcoma

        for item in STAGES:
            if self.icd == item['icd']:
                 if item['t'] is None:
                     self.t_set.add(STAGES[item['icd']])
                 else:
                     self.t_set.add(item['t'])

                 self.n_set.add(item['n'])
                 self.m_set.add(item['m'])
                 self.dukes_set.add(item['dukes'])
                 self.psa_set.add(item['psa'])
                 self.gleason_set.add(item['gleason'])
                 self.carcinosarcoma_set.add(item['carcinosarcoma'])
                 self.stages_dict[item['t'] + item['n'] + item['m'] + item['dukes'] + item['psa'] + item['gleason'] + item['carcinosarcoma']] = item['stage']

        if self.t is not None:
            self.validate_tnm()
            self.staging()


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

def tnm_stage(icd, t=None, n=None, m=None, dukes=None, psa=None, gleason=None, carcinosarcoma=None):
    icd = icd.strip()
    stager = GenericStager(icd, t, n, m, dukes, psa, gleason, carcinosarcoma)
    return stager.t

def remove_duplicates(l):
    return list(set(l))

def tnm_t(icd):
    retornar = []
    codigo = icd.split('.')[0].upper()
    for i in range(1, len(TUMOR_t)):
        num = TUMOR_t[i]
        i = i + 1
        vetor.append(num)
        dic = vetor

    retorno = dic

    for i in range(1, len(retorno)):
        valor = retorno[i]

        if valor['icd'] == codigo:
            retornar.append(valor['t'])

        i = i + 1

    retornar = remove_duplicates(retornar)
    return retornar

def tnm_n(icd):
    retornar = []
    codigo = icd.split('.')[0].upper()
    for i in range(1, len(NODES_n)):
        num = NODES_n[i]
        i = i + 1
        vetor.append(num)
        dic = vetor

    retorno = dic

    for i in range(1, len(retorno)):
        valor = retorno[i]

        if valor['icd'] == codigo:
            retornar.append(valor['n'])

        i = i + 1

    retornar = remove_duplicates(retornar)
    return retornar


def tnm_m(icd):
    retornar = []
    codigo = icd.split('.')[0].upper()
    for i in range(1, len(METASTASES_m)):
        num = METASTASES_m[i]
        i = i + 1
        vetor.append(num)
        dic = vetor

    retorno = dic

    for i in range(1, len(retorno)):
        valor = retorno[i]

        if valor['icd'] == codigo:
            retornar.append(valor['m'])

        i = i + 1

    retornar = remove_duplicates(retornar)
    return retornar
