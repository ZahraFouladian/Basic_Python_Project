import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"\"https?://(?:www\.)?youtube\.com/embed/(\w+)\""
    if link := re.search(pattern, s):
        output = "https://youtu.be/" + link.group(1)
        return output


if __name__ == "__main__":
    main()
