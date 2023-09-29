def main():
    import random

    guess_number = random.randint(1, 100)
    while True:
        try:
            level = int(input("Level:"))
            if level < 0:
                continue
            else:
                while True:
                    try:
                        number = int(input("Guess:"))
                        if number > guess_number:
                            print("Too large!")
                        elif number < guess_number:
                            print("Too small!")
                        else:
                            print("Just right!")
                            return True
                    except:
                        continue
        except:
            continue


if __name__ == "__main__":
    main()
