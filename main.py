import csv

with open('scientist.txt', encoding='utf8', ) as file:
    reader = csv.reader(file, delimiter='#')
    answer = list(reader)[1:]
    preparation_date = {}
    print(answer)
    for person in answer:
        date = person[-2]
        preparation = person[-3]
        if date < preparation_date.get(preparation, '99999999999999999999'):
            answer.remove(person)
    print(answer)

