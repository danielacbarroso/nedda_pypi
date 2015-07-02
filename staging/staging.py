# -*- coding: utf-8 -*-
from breast import *
from cervix_uteri import *
from colon_rectum import *
from prostate import *
from lung import *

def tnm_stage(icd, t, n, m, dukes=None, psa=None, gleasson=None):
    icd = icd.strip()

    if icd in BREAST_CANCER_ICDS:
        stager = BreastCancerStager(icd, t, n, m)
    elif icd in CERVIX_UTERI_CANCER_ICDS:
        stager = CervixUteriStager(icd, t, n, m)
    elif icd in COLON_CANCER_ICDS:
        stager = ColonRectumStager(icd, t, n, m, dukes)
    elif icd in PROSTATE_CANCER_ICDS:
        stager = ProstageCancerStager(icd, t, n, m, psa, gleasson)
    elif icd in LUNG_CANCER_ICDS:
        stager = LungCancerStager(icd, t, n, m)
    return stager.stage


if __name__ == '__main__':
    print tnm_stage('C50.0', 'Tis', 'N0', 'M0')
    print tnm_stage('C53.0', 'Tis', 'N0', 'M0')





