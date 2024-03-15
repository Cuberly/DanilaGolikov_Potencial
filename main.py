import csv

with open('scientist.txt', encoding='utf8', ) as file:
    reader = csv.reader(file, delimiter='#')
    answer = list(reader)[1:]
    print(answer)
    preparation_date = {}
    for ScientistName, preparation, date, componentsin in answer:
        if date < preparation.get(date, 0):
        count_class[level] = count_class.get(level, 0) + 1
        sum_class[level] = sum_class.get(level, 0) + (int(score) if score != 'None' else 0)