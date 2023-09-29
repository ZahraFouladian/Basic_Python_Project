def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (1 < len(s) and len(s) < 7):
        return False
    if not (s[0:2].isalpha()):
        return False
    for i in range(2, len(s)):
        if s[i].isnumeric():
            if not (s[i:].isnumeric()):
                return False
            if s[i:].startswith("0"):
                return False
            else:
                return True
    return True


if __name__ == "__main__":
    main()
