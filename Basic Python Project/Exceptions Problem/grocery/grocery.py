def main():
    items = dict()
    while True:
        try:
            item = input().upper()
            items[item] = items.get(item, 0) + 1

        except EOFError:
            list_items = list(items.keys())
            list_items.sort()
            for i in list_items:
                print(f"{items[i]} {i}")
            return True


if __name__ == "__main__":
    main()
