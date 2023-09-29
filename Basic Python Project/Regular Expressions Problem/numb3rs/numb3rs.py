import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        ip_list = ip.strip().split(".")
        if len(ip_list) == 4:
            for i in ip_list:
                i = int(i)
                if i < 0 or i > 255:
                    return False
            return True
        else:
            return False

    except:
        return False


if __name__ == "__main__":
    main()
