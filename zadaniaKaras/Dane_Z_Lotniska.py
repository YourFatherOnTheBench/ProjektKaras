import csv
from operator import itemgetter

network = {}
select_month = 1

with open('lotnisko.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
            print(row)
        

print(network)