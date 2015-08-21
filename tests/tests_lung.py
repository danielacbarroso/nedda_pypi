# -*- coding: utf-8 -*-
import unittest as ut
from nedda.staging.staging import tnm_stage


class Testtnm_stage(ut.TestCase):

    def test_lung_cancer_0(self):
        self.assertEquals('0', tnm_stage('C34.0', 'Tis', 'N0', 'M0'))
    
    def test_lung_cancer_IA(self):
        self.assertEquals('IA', tnm_stage('C34.0', 'T1a', 'N0', 'M0'))
        self.assertEquals('IA', tnm_stage('C34.0', 'T1b', 'N0', 'M0'))
        
    def test_lung_cancer_IB(self):
        self.assertEquals('IB', tnm_stage('C34.0', 'T2a', 'N0', 'M0'))        
        
    def test_lung_cancer_IIA(self):
        self.assertEquals('IIA', tnm_stage('C34.0', 'T2b', 'N0', 'M0'))
        self.assertEquals('IIA', tnm_stage('C34.0', 'T1a', 'N1', 'M0'))
        self.assertEquals('IIA', tnm_stage('C34.0', 'T1b', 'N1', 'M0'))
        self.assertEquals('IIA', tnm_stage('C34.0', 'T2a', 'N1', 'M0'))
        
    def test_lung_cancer_IIB(self):
        self.assertEquals('IIB', tnm_stage('C34.0', 'T2b', 'N1', 'M0'))
        self.assertEquals('IIB', tnm_stage('C34.0', 'T3', 'N0', 'M0'))
        
    def test_lung_cancer_IIIA(self):
        self.assertEquals('IIIA', tnm_stage('C34.0', 'T1a', 'N2', 'M0'))
        self.assertEquals('IIIA', tnm_stage('C34.0', 'T1b', 'N2', 'M0'))
        self.assertEquals('IIIA', tnm_stage('C34.0', 'T2a', 'N2', 'M0'))
        self.assertEquals('IIIA', tnm_stage('C34.0', 'T2b', 'N2', 'M0'))
        self.assertEquals('IIIA', tnm_stage('C34.0', 'T3', 'N1', 'M0'))
        self.assertEquals('IIIA', tnm_stage('C34.0', 'T3', 'N2', 'M0'))
        self.assertEquals('IIIA', tnm_stage('C34.0', 'T4', 'N0', 'M0'))
        self.assertEquals('IIIA', tnm_stage('C34.0', 'T4', 'N1', 'M0'))
        
    def test_lung_cancer_IIIB(self):   
        self.assertEquals('IIIB', tnm_stage('C34.0', 'T1a', 'N3', 'M0'))
        self.assertEquals('IIIB', tnm_stage('C34.0', 'T1b', 'N3', 'M0'))
        self.assertEquals('IIIB', tnm_stage('C34.0', 'T2a', 'N3', 'M0'))
        self.assertEquals('IIIB', tnm_stage('C34.0', 'T2b', 'N3', 'M0'))
        self.assertEquals('IIIB', tnm_stage('C34.0', 'T3', 'N3', 'M0'))      
        self.assertEquals('IIIB', tnm_stage('C34.0', 'T4', 'N2', 'M0'))      
        self.assertEquals('IIIB', tnm_stage('C34.0', 'T4', 'N3', 'M0'))

    def test_lung_cancer_IV(self):
        self.assertEquals('IV', tnm_stage('C34.0', 'Tis', 'N0', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T1a', 'N0', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T1b', 'N0', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T2a', 'N0', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T2b', 'N0', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T1a', 'N1', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T1b', 'N1', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T2a', 'N1', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T2b', 'N1', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T3', 'N0', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T1a', 'N2', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T1b', 'N2', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T2a', 'N2', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T2b', 'N2', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T3', 'N1', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T3', 'N2', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T4', 'N0', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T4', 'N1', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T1a', 'N3', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T1b', 'N3', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T2a', 'N3', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T2b', 'N3', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T3', 'N3', 'M1a'))      
        self.assertEquals('IV', tnm_stage('C34.0', 'T4', 'N2', 'M1a'))      
        self.assertEquals('IV', tnm_stage('C34.0', 'T4', 'N3', 'M1a'))
        self.assertEquals('IV', tnm_stage('C34.0', 'Tis', 'N0', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T1a', 'N0', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T1b', 'N0', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T2a', 'N0', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T2b', 'N0', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T1a', 'N1', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T1b', 'N1', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T2a', 'N1', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T2b', 'N1', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T3', 'N0', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T1a', 'N2', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T1b', 'N2', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T2a', 'N2', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T2b', 'N2', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T3', 'N1', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T3', 'N2', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T4', 'N0', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T4', 'N1', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T1a', 'N3', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T1b', 'N3', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T2a', 'N3', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T2b', 'N3', 'M1b'))
        self.assertEquals('IV', tnm_stage('C34.0', 'T3', 'N3', 'M1b'))      
        self.assertEquals('IV', tnm_stage('C34.0', 'T4', 'N2', 'M1b'))      
        self.assertEquals('IV', tnm_stage('C34.0', 'T4', 'N3', 'M1b'))
