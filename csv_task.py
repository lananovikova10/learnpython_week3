#Создайте список словарей:
#Запишите содержимое списка словарей в файл в формате csv
import csv

persons = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('export.csv','w',encoding='utf8') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter = ';')
    writer.writeheader()
    for person in persons:
        writer.writerow(person)


