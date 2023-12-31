def main():
    name_list = []
    while True:
        try:
            name = input("Name:")
            name_list.append(name)

        except EOFError:
            if len(name_list) == 1:
                print(f"Adieu, adieu, to {name_list[0]}")
            elif len(name_list) == 2:
                print(f"Adieu, adieu, to {name_list[0]} and {name_list[1]}")
            else:
                print(f"Adieu, adieu, to {name_list[0]}", end="")
                for i in name_list[1 : len(name_list) - 1]:
                    print(f", {i}", end="")
                print(f", and {name_list[-1]}")
            return True


if __name__ == "__main__":
    main()
