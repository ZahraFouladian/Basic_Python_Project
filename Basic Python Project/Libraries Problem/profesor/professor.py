import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        total = 0
        number_1 = generate_integer(level)
        number_2 = generate_integer(level)
        for j in range(3):
            print(f"{number_1} + {number_2} = ", end="")
            total = int(input())
            if total == (number_1 + number_2):
                score = score + 1
                break
            elif j == 2:
                print("EEE")
                print(f"{number_1} + {number_2} = {number_1 + number_2}")
            else:
                print("EEE")
    print(f"score:{score}")


def get_level():
    while True:
        try:
            Level = int(input("Level:"))
            if Level not in [1, 2, 3]:
                raise Exeption
        except:
            continue
        return Level


def generate_integer(Level):
    if Level == 1:
        number = random.randint(0, 10)
    elif Level == 2:
        number = random.randint(10, 100)
    else:
        number = random.randint(100, 1000)
    return number


if __name__ == "__main__":
    main()
