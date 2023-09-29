def main():
    time = input("What time is it?")
    time = convert(time)
    if 7 <= time and time <= 8:
        print("breakfast time")
    elif 12 <= time and time <= 13:
        print("lunch time")
    elif 18 <= time and time <= 20:
        print("dinner time ")


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
