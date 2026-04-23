import csv
import json

with open('departments.csv', encoding='utf-8') as file:
    dct1 = {}
    reader = csv.DictReader(file, delimiter=';')

    for row in reader:
        exp = int(row['experience'])
        spec = row['specialization']
        budget = int(row['budget'])
        department = row['department']
        if department not in dct1.keys():
            dct1[department] = {
                'specialization': spec,
                'budget': budget,
                'experience': exp
            }
        else:
            if spec > dct1[department]['specialization']:
                dct1[department]['specialization'] = spec
            if exp > dct1[department]['experience']:
                dct1[department]['experience'] = exp
            dct1[department]['budget'] += budget


        with open('report.json', mode='w', encoding='utf-8') as file2:
            json.dump(dct1, file2, ensure_ascii=False, indent=2)




