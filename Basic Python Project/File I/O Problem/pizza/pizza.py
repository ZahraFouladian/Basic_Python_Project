from sys import argv, exit
from tabulate import tabulate
import csv

# check argv is valid or csv file
if len(argv) < 2:
    exit("Too few command-line arguments")
elif len(argv) > 2:
    exit("Too many command-line arguments")
else:
    if not (argv[1].endswith(".csv")):
        exit("Not a CSV file")

file = argv[1]

try:
    table_file = []
    with open(file) as f:
        read_file = csv.reader(f)
        headers_file = list(next(read_file))
        for i in read_file:
            table_file.append([i[0], i[1], i[2]])
            print(tabulate(table_file, headers_file, tablefmt="grid"))


except FileNotFoundError:
    exit("File does not exist")








with open(w_file, "w") as file:
    w = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    w.writeheader()
    len_firstnames = len(firstnames)
    for i in range(len_firstnames):
        name_house_dict = {
            "first": firstnames[i],
            "last": lastnames[i],
            "house": house[i],
        }
        w.writerow(name_house_dict)
