import csv
from nedda.tests.tests_colon import Testtnm_stage

icds_set = set()
stages_dict_list = list()

with open('stages.csv', 'rt') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        icds_set.add(row[0])
        stages_dict_list.append(
                {
                    'icd': row[0],
                    't': row[1],
                    'n': row[2],
                    'm': row[3],
                    'stage': row[5],
                    'psa': row[6],
                    'gleason': row[7]
                })
print stages_dict_list
