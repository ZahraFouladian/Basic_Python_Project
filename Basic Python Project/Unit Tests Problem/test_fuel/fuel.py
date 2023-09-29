def main():
    while True:
        try:
            percentage = convert(input())
        except:
            pass
        else:
            break
    print(gauge(percentage))


def convert(fraction):
    fraction= fraction.split('/')
    x = int(fraction[0])
    y = int(fraction[1])
    if y == 0:
        raise ZeroDivisionError
    elif y < x:
        raise ValueError
    return int(round((x/y)*100))



def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return str(percentage)


if __name__ == "__main__":
    main()
