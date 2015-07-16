# -*- coding: utf-8 -*-
from .breast import *
from .cervix_uteri import *
from .colon_rectum import *
from .prostate import *
from .lung import *
from .corpus_uteri_sarcomas import *
from .corpus_uteri_carcinomas import *
from .stomach import *

def tnm_stager_factory(icd, t, n, m, dukes=None, psa=None, gleason=None):
    icd = icd.strip()
    stager = None

    if icd in BREAST_CANCER_ICDS:
        stager = BreastCancerStager(icd, t, n, m)
    elif icd in CERVIX_UTERI_CANCER_ICDS:
        stager = CervixUteriStager(icd, t, n, m)
    elif icd in COLON_CANCER_ICDS:
        stager = ColonRectumStager(icd, t, n, m, dukes)
    elif icd in CORPUS_UTERI_CANCER_ICDS:
        stager = CorpusUteriCarcinomaStager(icd, t, n, m)
    elif icd in PROSTATE_CANCER_ICDS:
        stager = ProstateCancerStager(icd, t, n, m, psa, gleason)
    elif icd in LUNG_CANCER_ICDS:
        stager = LungCancerStager(icd, t, n, m)
    elif icd in STOMACH_CANCER_ICDS:
        stager = StomachCancerStager(icd, t, n, m)
    return stager


def tnm_stage(icd, t, n, m, dukes=None, psa=None, gleason=None):
    icd = icd.strip()
    stager = None

    if icd in BREAST_CANCER_ICDS:
        stager = BreastCancerStager(icd, t, n, m)
    elif icd in CERVIX_UTERI_CANCER_ICDS:
        stager = CervixUteriStager(icd, t, n, m)
    elif icd in COLON_CANCER_ICDS:
        stager = ColonRectumStager(icd, t, n, m, dukes)
    elif icd in CORPUS_UTERI_CANCER_ICDS:
        stager = CorpusUteriCarcinomaStager(icd, t, n, m)
    elif icd in PROSTATE_CANCER_ICDS:
        stager = ProstateCancerStager(icd, t, n, m, psa, gleason)
    elif icd in LUNG_CANCER_ICDS:
        stager = LungCancerStager(icd, t, n, m)
    elif icd in STOMACH_CANCER_ICDS:
        stager = StomachCancerStager(icd, t, n, m)
    return stager.stage