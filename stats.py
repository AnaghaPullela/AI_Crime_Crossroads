from data_utils import data

crimes = []

for item in data:
    if (item[' PRIMARY DESCRIPTION'] not in crimes):
        crimes.append(item[' PRIMARY DESCRIPTION'])
        