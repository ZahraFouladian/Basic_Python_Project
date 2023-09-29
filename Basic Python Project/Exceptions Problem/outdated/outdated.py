def main():
    check = 0
    while not check:
        date = input("Date: ")
        check = check_valid_data(date)
        if check:
            print(f"{check[2]}-{check[1]:02}-{check[1]-1:02}")


def check_valid_data(date):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    date = date.replace(",", " ")
    date = date.replace("/", " ")
    month, day, year = date.split()

    try:
        if month.isalpha():
            month = month.title()
            if month in months:
                month = months.index(month) + 1
                day = int(day)
                year = int(year)
                if month > 12 or day > 31:
                    return False
            else:
                return False
        else:
            month = int(month)
            day = int(day)
            year = int(year)
            if month > 12 or day > 31:
                return False
    except:
        return False
    else:
        return [day, month, year]


if __name__ == "__main__":
    main()
