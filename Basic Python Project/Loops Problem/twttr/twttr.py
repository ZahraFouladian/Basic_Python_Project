def main():
    text = input("Text:")
    for i in "aeiouAEIOU":
        text = text.replace(i, "")
    print(text)


if __name__ == "__main__":
    main()
