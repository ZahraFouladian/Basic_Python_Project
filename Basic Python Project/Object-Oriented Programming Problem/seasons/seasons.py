import inflect
import operator
from sys import exit
from datetime import date

def main():
    birth = input("Date of Birth: ")
    days = days_diffrence(birth)
    if not(days):
        exit("Invalid date")
    print(days)


def days_diffrence(birth):
    try:
        day = operator.sub(date.today(), date.fromisoformat(birth))
        minutes = day.days * 24 * 60
        a = inflect.engine()
        minutes = (a.number_to_words(minutes, andword="")).capitalize()
        return f"{minutes} minutes"

    except ValueError:
        return False



if __name__ == "__main__":
    main()
