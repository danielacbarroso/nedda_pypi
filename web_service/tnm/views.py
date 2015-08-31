import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from nedda.staging.staging import GenericStager
#from .models import Cid, Tnm
from django.core import serializers
from nedda.staging.staging import STAGES
from nedda.staging import staging
from nedda.staging.staging import tnm_stage
import csv, os

icd_list_set = set()

def calcula(request):
    return render(request, "calcula.html")

def get_icds(request):

    icd_list = []
    if len(icd_list_set) == 0:

        for item in STAGES:
            icd_list_set.add(item['icd'])

        icd_list = list(icd_list_set)
        icd_list.sort()

    request_data = {
        'request_status': 'success',
        'icd_list': icd_list,
    }

    return HttpResponse(json.dumps(request_data), content_type='application/json')

def get_icds_neoplasm(request):


    icd_list_neoplasm = staging.tnm_neoplasms()

    request_data = {
        'request_status': 'success',
        'icd_list_neoplasm': icd_list_neoplasm,
    }

    return HttpResponse(json.dumps(request_data), content_type='application/json')

def get_tnms(request, icd):

    # gs = GenericStager(icd.split('-')[0].strip())
    gs = GenericStager(icd)
    request_data = {
        'request_status': 'success',
        # 'icd_list_neoplasm' : gs.neoplasms_set,
        'ts_list': gs.get_t_list(),
        'ns_list': gs.get_n_list(),
        'ms_list': gs.get_m_list(),
        'dukes_list': list(gs.dukes_set),
        'psa_list': sorted(gs.psa_set),
        'gleason_list': sorted(gs.gleason_set),
    }

    return HttpResponse(json.dumps(request_data), content_type='application/json')

def get_stage(request, icd, t, n, m, dukes=None, psa=None, gleason=None):
    stage = ''
    if icd == 'C18':
        if dukes == '-':
            dukes = ''
            stage = tnm_stage(icd, t, n, m, dukes)
        stage = tnm_stage(icd, t, n, m, dukes)

    elif icd == 'C61':
        if psa != '-' and gleason != '-':
            stage = tnm_stage(icd, t, n, m, None, psa, gleason)
        elif psa != '-' and gleason == '-':
            gleason = ''
            stage = tnm_stage(icd, t, n, m, None, psa, gleason)
        elif psa == '-' and gleason != '-':
            psa = ''
            stage = tnm_stage(icd, t, n, m, None, psa, gleason)
        else:
            psa=''
            gleason=''
            stage = tnm_stage(icd, t, n, m, None, psa, gleason)

    else:
        stage = tnm_stage(icd, t, n, m)
    stage1 = stage

    if stage1 == None:
        stage = 'undefined'
    stage = 'Staging ' + stage

    request_data = {
        'request_status': 'success',
        'stage': stage
    }

    return HttpResponse(json.dumps(request_data), content_type='application/json')