from sys import argv, exit

# check argv is valid
if len(argv) < 2:
    exit("Too few command-line arguments")
elif len(argv) > 2:
    exit("Too many command-line arguments")
else:
    if not (argv[1].endswith(".py")):
        exit("Not a python file")


file = argv[1]

try:
    line_number = 0
    with open(file) as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith("#"):
                continue
            elif line == "":
                continue
            else:
                line_number = line_number + 1
except FileNotFoundError:
    exit("File does not exist")
print(line_number)
