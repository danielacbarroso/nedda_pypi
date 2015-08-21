# -*- coding: utf-8 -*-
import unittest as ut
from nedda.staging.staging import tnm_stage


class Testtnm_stage(ut.TestCase):

    def test_cervix_uteri_cancer_0(self):
        self.assertEquals('0', tnm_stage('C53.0', 'Tis', 'N0', 'M0'))

    def test_cervix_uteri_cancer_I(self):
        self.assertEquals('I', tnm_stage('C53.0', 'T1', 'N0', 'M0'))

    def test_cervix_uteri_cancer_IA(self):
        self.assertEquals('IA', tnm_stage('C53.0', 'T1a', 'N0', 'M0'))

    def test_cervix_uteri_cancer_IA1(self):
        self.assertEquals('IA1', tnm_stage('C53.0', 'T1a1', 'N0', 'M0'))

    def test_cervix_uteri_cancer_IA2(self):
        self.assertEquals('IA2', tnm_stage('C53.0', 'T1a2', 'N0', 'M0'))

    def test_cervix_uteri_cancer_IB(self):
        self.assertEquals('IB', tnm_stage('C53.0', 'T1b', 'N0', 'M0'))

    def test_cervix_uteri_cancer_IB1(self):
        self.assertEquals('IB1', tnm_stage('C53.0', 'T1b1', 'N0', 'M0'))

    def test_cervix_uteri_cancer_IB2(self):
        self.assertEquals('IB2', tnm_stage('C53.0', 'T1b2', 'N0', 'M0'))

    def test_cervix_uteri_cancer_II(self):
        self.assertEquals('II', tnm_stage('C53.0', 'T2', 'N0', 'M0'))

    def test_cervix_uteri_cancer_IIA(self):
        self.assertEquals('IIA', tnm_stage('C53.0', 'T2a', 'N0', 'M0'))

    def test_cervix_uteri_cancer_IIA1(self):
        self.assertEquals('IIA1', tnm_stage('C53.0', 'T2a1', 'N0', 'M0'))

    def test_cervix_uteri_cancer_IIA2(self):
        self.assertEquals('IIA2', tnm_stage('C53.0', 'T2a2', 'N0', 'M0'))

    def test_cervix_uteri_cancer_IIB(self):
        self.assertEquals('IIB', tnm_stage('C53.0', 'T2b', 'N0', 'M0'))

    def test_cervix_uteri_cancer_III(self):
        self.assertEquals('III', tnm_stage('C53.0', 'T3', 'N0', 'M0'))

    def test_cervix_uteri_cancer_IIIA(self):
        self.assertEquals('IIIA', tnm_stage('C53.0', 'T3a', 'N0', 'M0'))

    def test_cervix_uteri_cancer_IIIB(self):
        self.assertEquals('IIIB', tnm_stage('C53.0', 'T3b', 'N0', 'M0'))
        self.assertEquals('IIIB', tnm_stage('C53.0', 'T3b', 'N1', 'M0'))
        self.assertEquals('IIIB', tnm_stage('C53.0', 'T1', 'N1', 'M0'))
        self.assertEquals('IIIB', tnm_stage('C53.0', 'T2', 'N1', 'M0'))
        self.assertEquals('IIIB', tnm_stage('C53.0', 'T3', 'N1', 'M0'))

    def test_cervix_uteri_cancer_IVA(self):
        self.assertEquals('IVA', tnm_stage('C53.0', 'T4', 'N0', 'M0'))
        self.assertEquals('IVA', tnm_stage('C53.0', 'T4', 'N1', 'M0'))

    def test_cervix_uteri_cancer_IVB(self):
        self.assertEquals('IVB', tnm_stage('C53.0', 'Tis', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C53.0', 'T1', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C53.0', 'T1a', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C53.0', 'T1a1', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C53.0', 'T1a2', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C53.0', 'T1b', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C53.0', 'T1b1', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C53.0', 'T1b2', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C53.0', 'T2', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C53.0', 'T2a', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C53.0', 'T2a1', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C53.0', 'T2a2', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C53.0', 'T2b', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C53.0', 'T3', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C53.0', 'T3a', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C53.0', 'T3b', 'N0', 'M1'))
        self.assertEquals('IVB', tnm_stage('C53.0', 'T4', 'N0', 'M1'))

