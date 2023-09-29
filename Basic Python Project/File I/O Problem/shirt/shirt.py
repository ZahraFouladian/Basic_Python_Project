# import library
from sys import argv, exit
import os
from PIL import ImageOps as imgops, Image as img


# check command-line argument
# check valid input and output and have same extensions


if len(argv) < 3:
    exit("Too few command-line arguments")
elif len(argv) > 3:
    exit("Too many command-line arguments")
else:
    if not (argv[1].lower().endswith((".jpg", ".jpeg", ".png"))):
        exit("Invalid intput")
    elif not (argv[2].lower().endswith((".jpg", ".jpeg", ".png"))):
        exit("Invalid output")
    else:
        _, extention_1 = argv[1].split(".")
        _, extention_2 = argv[2].split(".")
        if extention_1 != extention_2:
            exit("Input and output have different extensions")


try:
    shirt = img.open("shirt.png")
    input_img = img.open(argv[1])
except FileNotFoundError:
    exit("Input does not exist")
except Exception as exp:
    exit(exp)

# make and save picture

input_img = imgops.fit(input_img, shirt.size)
input_img.paste(shirt, shirt)
input_img.save(argv[2])
