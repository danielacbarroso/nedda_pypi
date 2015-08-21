# -*- coding: utf-8 -*-
import unittest as ut
from nedda.staging.staging import tnm_stage


class Testtnm_stage(ut.TestCase):

    def test_corpus_uteri_sarcomas_cancer_I(self):
        self.assertEquals('I', tnm_stage('C54.0', 'T1', 'N0', 'M0'))

    def test_corpus_uteri_sarcomas_cancer_IA(self):
        self.assertEquals('IA', tnm_stage('C54.0', 'T1a', 'N0', 'M0'))

    def test_corpus_uteri_sarcomas_cancer_IB(self):
        self.assertEquals('IB', tnm_stage('C54.0', 'T1b', 'N0', 'M0'))

    def test_corpus_uteri_sarcomas_cancer_IC(self):
        self.assertEquals('IC', tnm_stage('C54.0', 'T1c', 'N0', 'M0'))

    def test_corpus_uteri_sarcomas_cancer_II(self):
        self.assertEquals('II', tnm_stage('C54.0', 'T2', 'N0', 'M0'))

    def test_corpus_uteri_sarcomas_cancer_IIIA(self):
        self.assertEquals('IIIA', tnm_stage('C54.0', 'T3a', 'N0', 'M0'))

    def test_corpus_uteri_sarcomas_cancer_IIIB(self):
        self.assertEquals('IIIB', tnm_stage('C54.0', 'T3b', 'N0', 'M0'))

    def test_corpus_uteri_sarcomas_cancer_IIIC(self):
        self.assertEquals('IIIC', tnm_stage('C54.0', 'T1', 'N1', 'M0'))
        self.assertEquals('IIIC', tnm_stage('C54.0', 'T2', 'N1', 'M0'))
        self.assertEquals('IIIC', tnm_stage('C54.0', 'T3', 'N1', 'M0'))

    def test_corpus_uteri_sarcomas_cancer_IVA(self):
        self.assertEquals('IVA', tnm_stage('C54.0', 'T4', 'N0', 'M0'))
        self.assertEquals('IVA', tnm_stage('C54.0', 'T4', 'N1', 'M0'))
        self.assertEquals('IVA', tnm_stage('C54.0', 'T4', 'N2', 'M0'))

    def test_corpus_uteri_sarcomas_cancer_IVB(self):
        self.assertEquals('IVB', tnm_stage('C54.0', 'T1', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T1a', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T1b', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T1c', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T2', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T3', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T3a', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T3b', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T4', 'N0', 'M1'))

        self.assertEquals('IVB', tnm_stage('C54.0', 'T1', 'N1', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T1a', 'N1', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T1b', 'N1', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T1c', 'N1', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T2', 'N1', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T3', 'N1', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T3a', 'N1', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T3b', 'N1', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T4', 'N1', 'M1'))

        self.assertEquals('IVB', tnm_stage('C54.0', 'T1', 'N2', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T1a', 'N2', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T1b', 'N2', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T1c', 'N2', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T2', 'N2', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T3', 'N2', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T3a', 'N2', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T3b', 'N2', 'M1'))
        self.assertEquals('IVB', tnm_stage('C54.0', 'T4', 'N2', 'M1'))