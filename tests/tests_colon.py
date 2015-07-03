__author__ = 'sandra'

import unittest as ut
from staging.staging import tnm_stage


class Testtnm_stage(ut.TestCase):

    def test_colon_cancer_0(self):
        self.assertEquals('0', tnm_stage('C18.0', 'Tis', 'N0', 'M0', None))

    def test_colon_cancer_I(self):
        self.assertEquals('I', tnm_stage('C18.0', 'T1', 'N0', 'M0', 'A'))
        self.assertEquals('I', tnm_stage('C18.0', 'T2', 'N0', 'M0', 'A'))

    def test_colon_cancer_IIA(self):
        self.assertEquals('IIA', tnm_stage('C18.0', 'T3', 'N0', 'M0', 'B'))

    def test_colon_cancer_IIB(self):
        self.assertEquals('IIB', tnm_stage('C18.0', 'T4a', 'N0', 'M0', 'B'))

    def test_colon_cancer_IIC(self):
        self.assertEquals('IIC', tnm_stage('C18.0', 'T4b', 'N0', 'M0', 'B'))

    def test_colon_cancer_IIIA(self):
        self.assertEquals('IIIA', tnm_stage('C18.0', 'T1-T2', 'N1', 'M0', 'C'))
        self.assertEquals('IIIA', tnm_stage('C18.0', 'T1-T2', 'N1c', 'M0', 'C'))
        self.assertEquals('IIIA', tnm_stage('C18.0', 'T1', 'N2a', 'M0', 'C'))

    def test_colon_cancer_IIIB(self):
        self.assertEquals('IIIB', tnm_stage('C18.0', 'T3-T4a', 'N1', 'M0', 'C'))
        self.assertEquals('IIIB', tnm_stage('C18.0', 'T3-T4a', 'N1c', 'M0', 'C'))
        self.assertEquals('IIIB', tnm_stage('C18.0', 'T2-T3', 'N2a', 'M0', 'C'))
        self.assertEquals('IIIB', tnm_stage('C18.0', 'T1-T2', 'N2b', 'M0', 'C'))

    def test_colon_cancer_IIIC(self):
        self.assertEquals('IIIC', tnm_stage('C18.0', 'T4a', 'N2a', 'M0', 'C'))
        self.assertEquals('IIIC', tnm_stage('C18.0', 'T3-T4a', 'N2b', 'M0', 'C'))
        self.assertEquals('IIIC', tnm_stage('C18.0', 'T4b', 'N1-N2', 'M0', 'C'))

    def test_colon_cancer_IVA(self):
        self.assertEquals('IVA', tnm_stage('C18.0', 'Tis', 'N0', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T1', 'N0', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T2', 'N0', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T3', 'N0', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4a', 'N0', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4b', 'N0', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T1-T2', 'N0', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T2-T3', 'N0', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T3-T4a', 'N0', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4a', 'N0', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4b', 'N0', 'M1a', None))

        self.assertEquals('IVA', tnm_stage('C18.0', 'Tis', 'N1', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T1', 'N1', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T2', 'N1', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T3', 'N1', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4a', 'N1', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4b', 'N1', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T1-T2', 'N1', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T2-T3', 'N1', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T3-T4a', 'N1', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4a', 'N1', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4b', 'N1', 'M1a', None))

        self.assertEquals('IVA', tnm_stage('C18.0', 'Tis', 'N1-N2', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T1', 'N1-N2', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T2', 'N1-N2', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T3', 'N1-N2', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4a', 'N1-N2', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4b', 'N1-N2', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T1-T2', 'N1-N2', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T2-T3', 'N1-N2', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T3-T4a', 'N1-N2', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4a', 'N1-N2', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4b', 'N1-N2', 'M1a', None))

        self.assertEquals('IVA', tnm_stage('C18.0', 'Tis', 'N1c', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T1', 'N1c', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T2', 'N1c', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T3', 'N1c', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4a', 'N1c', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4b', 'N1c', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T1-T2', 'N1c', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T2-T3', 'N1c', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T3-T4a', 'N1c', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4a', 'N1c', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4b', 'N1c', 'M1a', None))

        self.assertEquals('IVA', tnm_stage('C18.0', 'Tis', 'N2b', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T1', 'N2b', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T2', 'N2b', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T3', 'N2b', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4a', 'N2b', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4b', 'N2b', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T1-T2', 'N2b', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T2-T3', 'N2b', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T3-T4a', 'N2b', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4a', 'N2b', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4b', 'N2b', 'M1a', None))

        self.assertEquals('IVA', tnm_stage('C18.0', 'Tis', 'N2a', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T1', 'N2a', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T2', 'N2a', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T3', 'N2a', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4a', 'N2a', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4b', 'N2a', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T1-T2', 'N2a', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T2-T3', 'N2a', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T3-T4a', 'N2a', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4a', 'N2a', 'M1a', None))
        self.assertEquals('IVA', tnm_stage('C18.0', 'T4b', 'N2a', 'M1a', None))

    def test_colon_cancer_IVB(self):
        self.assertEquals('IVB', tnm_stage('C18.0', 'Tis', 'N0', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T1', 'N0', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T2', 'N0', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T3', 'N0', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4a', 'N0', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4b', 'N0', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T1-T2', 'N0', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T2-T3', 'N0', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T3-T4a', 'N0', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4a', 'N0', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4b', 'N0', 'M1b', None))

        self.assertEquals('IVB', tnm_stage('C18.0', 'Tis', 'N1', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T1', 'N1', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T2', 'N1', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T3', 'N1', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4a', 'N1', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4b', 'N1', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T1-T2', 'N1', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T2-T3', 'N1', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T3-T4a', 'N1', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4a', 'N1', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4b', 'N1', 'M1b', None))

        self.assertEquals('IVB', tnm_stage('C18.0', 'Tis', 'N1-N2', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T1', 'N1-N2', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T2', 'N1-N2', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T3', 'N1-N2', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4a', 'N1-N2', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4b', 'N1-N2', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T1-T2', 'N1-N2', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T2-T3', 'N1-N2', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T3-T4a', 'N1-N2', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4a', 'N1-N2', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4b', 'N1-N2', 'M1b', None))

        self.assertEquals('IVB', tnm_stage('C18.0', 'Tis', 'N1c', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T1', 'N1c', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T2', 'N1c', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T3', 'N1c', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4a', 'N1c', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4b', 'N1c', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T1-T2', 'N1c', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T2-T3', 'N1c', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T3-T4a', 'N1c', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4a', 'N1c', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4b', 'N1c', 'M1b', None))

        self.assertEquals('IVB', tnm_stage('C18.0', 'Tis', 'N2b', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T1', 'N2b', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T2', 'N2b', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T3', 'N2b', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4a', 'N2b', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4b', 'N2b', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T1-T2', 'N2b', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T2-T3', 'N2b', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T3-T4a', 'N2b', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4a', 'N2b', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4b', 'N2b', 'M1b', None))

        self.assertEquals('IVB', tnm_stage('C18.0', 'Tis', 'N2a', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T1', 'N2a', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T2', 'N2a', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T3', 'N2a', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4a', 'N2a', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4b', 'N2a', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T1-T2', 'N2a', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T2-T3', 'N2a', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T3-T4a', 'N2a', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4a', 'N2a', 'M1b', None))
        self.assertEquals('IVB', tnm_stage('C18.0', 'T4b', 'N2a', 'M1b', None))