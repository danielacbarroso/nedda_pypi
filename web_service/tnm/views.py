import json
from django.shortcuts import render
from django.http import HttpResponse
from staging.staging import GenericStager
from staging.staging import STAGES
from staging.staging import tnm_stage

icd_list_set = set()


def calcula(request):
    return render(request, "calcula.html")


def get_icds(request):

    icd_list = []

    if len(icd_list_set) == 0:
        for item in STAGES:
            icd_list.append(item['icd'] + ' - ' + item['neoplasms'])

        icd_list = set(icd_list)

    request_data = {
        'request_status': 'success',
        'icd_list': sorted(icd_list),
    }

    return HttpResponse(json.dumps(request_data), content_type='application/json')


def get_tnms(request, icd):

    icd = icd.split('-')[0].strip()

    gs = GenericStager(icd)

    request_data = {
        'request_status': 'success',
        'ts_list': gs.get_t_list(),
        'ns_list': gs.get_n_list(),
        'ms_list': gs.get_m_list(),
        'dukes_list': gs.get_dukes_list(),
        'psa_list': gs.get_psa_list(),
        'gleason_list': gs.get_gleason_list(),
    }

    return HttpResponse(json.dumps(request_data), content_type='application/json')


def get_stage(request, icd, t, n, m, dukes=None, psa=None, gleason=None):

    if dukes == u'undefined' or dukes=='-':
        dukes = None
    if psa == u'undefined' or psa=='-':
        psa = None
    if gleason == u'undefined' or gleason=='-':
        gleason = None

    if icd == 'C54 - Corpus Uteri Carcinomas':
        carcinosarcoma = 'C'
    elif icd == 'C54 - Corpus Uteri Sarcomas':
        carcinosarcoma = 'S'
    else:
        carcinosarcoma = None

    stage = tnm_stage(icd, t, n, m, dukes=dukes, psa=psa, gleason=gleason, carcinosarcoma=carcinosarcoma)

    if stage == None:
        stage = 'undefined'
    stage = 'Staging ' + stage

    request_data = {
        'request_status': 'success',
        'stage': stage
    }

    return HttpResponse(json.dumps(request_data), content_type='application/json')
