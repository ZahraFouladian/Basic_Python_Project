def main():
    while True:
        try:
            fraction = input("Fraction: ").split("/")
            fraction = round(int(fraction[0]) / int(fraction[1]) * 100)
            if fraction > 100:
                raise ValueError
            if fraction >= 99:
                print("F")
                return True
            elif fraction <= 1:
                print("E")
                return True

            else:
                print(f"{fraction}%")
                return True

        except (ZeroDivisionError, ValueError):
            continue


if __name__ == "__main__":
    main()
