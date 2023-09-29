def main():
    text = camel_to_snake(input("camelCase: "))
    print(text)


def camel_to_snake(text):
    new_text = ""
    for i in text:
        new_text = new_text + "_" + i.lower() if i.isupper() else new_text + i
    return new_text


if __name__ == "__main__":
    main()
