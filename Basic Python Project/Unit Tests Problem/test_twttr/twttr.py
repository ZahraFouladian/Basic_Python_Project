def main():
    text = input("Text:")
    new_text = shorten(text)
    print(text)

def shorten(text):
    for i in "aeiouAEIOU":
        text = text.replace(i, "")
    return text

if __name__ == "__main__":
    main()
