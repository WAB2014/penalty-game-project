import csv
with open('footieINFO.csv', 'r') as file:
    reader = csv.reader(file)
    i = 0
    for row in reader:
        print(', '.join(row[1:7]))
        if i == 5:
            break
        i += 1

