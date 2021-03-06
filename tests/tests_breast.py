# -*- coding: utf-8 -*-
import unittest as ut
from nedda.staging.staging import tnm_stage


class Testtnm_stage(ut.TestCase):

    def test_breast_cancer_0(self):
        self.assertEquals('0', tnm_stage('C50.0', 'Tis', 'N0', 'M0'))
    
    def test_breast_cancer_IA(self):
        self.assertEquals('IA', tnm_stage('C50.0', 'T1', 'N0', 'M0'))
        
    def test_breast_cancer_IB(self):
        self.assertEquals('IB', tnm_stage('C50.0', 'T0', 'N1mi', 'M0'))
        self.assertEquals('IB', tnm_stage('C50.0', 'T1', 'N1mi', 'M0'))
        
    def test_breast_cancer_IIA(self):
        self.assertEquals('IIA', tnm_stage('C50.0', 'T0', 'N1', 'M0'))
        self.assertEquals('IIA', tnm_stage('C50.0', 'T1', 'N1', 'M0'))
        self.assertEquals('IIA', tnm_stage('C50.0', 'T2', 'N0', 'M0'))
        
    def test_breast_cancer_IIB(self):
        self.assertEquals('IIB', tnm_stage('C50.0', 'T2', 'N1', 'M0'))
        self.assertEquals('IIB', tnm_stage('C50.0', 'T3', 'N0', 'M0'))
        
    def test_breast_cancer_IIIA(self):
        self.assertEquals('IIIA', tnm_stage('C50.0', 'T0', 'N2', 'M0'))
        self.assertEquals('IIIA', tnm_stage('C50.0', 'T1', 'N2', 'M0'))
        self.assertEquals('IIIA', tnm_stage('C50.0', 'T2', 'N2', 'M0'))
        self.assertEquals('IIIA', tnm_stage('C50.0', 'T3', 'N1', 'M0'))
        self.assertEquals('IIIA', tnm_stage('C50.0', 'T3', 'N2', 'M0'))
        
    def test_breast_cancer_IIIB(self):   
        self.assertEquals('IIIB', tnm_stage('C50.0', 'T4', 'N0', 'M0'))
        self.assertEquals('IIIB', tnm_stage('C50.0', 'T4', 'N1', 'M0'))
        self.assertEquals('IIIB', tnm_stage('C50.0', 'T4', 'N2', 'M0'))
        
    def test_breast_cancer_IIIC(self):   
        self.assertEquals('IIIC', tnm_stage('C50.0', 'Tis', 'N3', 'M0'))
        self.assertEquals('IIIC', tnm_stage('C50.0', 'T1', 'N3', 'M0'))
        self.assertEquals('IIIC', tnm_stage('C50.0', 'T2', 'N3', 'M0'))
        self.assertEquals('IIIC', tnm_stage('C50.0', 'T3', 'N3', 'M0'))
        
    def test_breast_cancer_IV(self):
        self.assertEquals('IV', tnm_stage('C50.0', 'T1', 'N0', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T0', 'N1mi', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T1', 'N1mi', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T0', 'N1', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T1', 'N1', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T2', 'N0', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T2', 'N1', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T3', 'N0', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T0', 'N2', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T1', 'N2', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T2', 'N2', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T3', 'N1', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T3', 'N2', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T4', 'N0', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T4', 'N1', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T4', 'N2', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'Tis', 'N3', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T1', 'N3', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T2', 'N3', 'M1'))
        self.assertEquals('IV', tnm_stage('C50.0', 'T3', 'N3', 'M1'))