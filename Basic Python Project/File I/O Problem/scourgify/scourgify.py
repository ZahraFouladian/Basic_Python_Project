from sys import argv, exit
import csv

# check argv is valid or csv file
if len(argv) < 3:
    exit("Too few command-line arguments")
elif len(argv) > 3:
    exit("Too many command-line arguments")
else:
    if not (argv[1].endswith(".csv")):
        exit("Not a CSV file")
    elif not (argv[2].endswith(".csv")):
        exit("Not a CSV file")


r_file = argv[1]
w_file = argv[2]
first_names = []
last_names = []
house = []

# read  file(before.csv)
try:
    with open(r_file, "r") as file:
        r = csv.DictReader(file)
        for row in r:
            name = row["name"].split(",")
            first_name = name[1].strip()
            last_name = name[0].strip()
            last_names.append(last_name)
            first_names.append(first_name)
            house.append(row["house"])
except FileNotFoundError:
    exit("File does not exist")
except Exception as arg:
    exit(arg)


# write file(after.csv)

with open(w_file, "w") as file:
    w = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    w.writeheader()
    len_first_names = len(first_names)
    for i in range(len_first_names):
        name_house_dict = {
            "first": first_names[i],
            "last": last_names[i],
            "house": house[i],
        }
        w.writerow(name_house_dict)
