# Seasons of Love
Assuming there are 365 days in a year, there are minutes in that same year (because there are 24 hours in a day and 60 minutes in an hour). But how many minutes are there in two or more years? Well, it depends on how many of those are leap years with 366 days, per the Gregorian calendar, as some of them could have additional minutes. In fact, how many minutes has it been since you were born? Well, that, too, depends on how many leap years there have been since! There is an algorithm for such, but let’s not reinvent that wheel. Let’s use a library instead. Fortunately, Python comes with a datetime module that has a class called date that can help, per docs.python.org/3/library/datetime.html#date-objects.

In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any and between words. Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.

Structure your program per the below, not only with a main function but also with one or more other functions as well:
```python

from datetime import date


def main():
    ...


...


if __name__ == "__main__":
    main()
```
You’re welcome to import other (built-in) libraries, or any that are specified in the below hints. Exit via sys.exit if the user does not input a date in YYYY-MM-DD format. Ensure that your program will not raise any exceptions.

Either before or after you implement seasons.py, additionally implement, in a file called test_seasons.py, one or more functions that test your implementation of any functions besides main in seasons.py thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

```python
pytest test_seasons.py
```


# Cookie Jar
Suppose that you’d like to implement a cookie jar in which to store cookies. In a file called jar.py, implement a class called Jar with these methods:
__init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
__str__ should return a str with 
 🍪, where 
 is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
capacity should return the cookie jar’s capacity.
size should return the number of cookies actually in the cookie jar, initially 0.
Structure your class per the below. You may not alter these methods’ parameters, but you may add your own methods.
```python

class Jar:
    def __init__(self, capacity=12):
        ...

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
```
Either before or after you implement jar.py, additionally implement, in a file called test_jar.py, four or more functions that collectively test your implementation of Jar thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_jar.py
Note that it’s not as easy to test instance methods as it is to test functions alone, since instance methods sometimes manipulate the same “state” (i.e., instance variables). To test one method (e.g., withdraw), then, you might need to call another method first (e.g., deposit). But the method you call first might itself not be correct!

And so programmers sometimes mock (i.e., simulate) state when testing methods, as with Python’s own mock object library, so that you can call just the one method but modify the underlying state first, without calling the other method to do so.

For simplicity, though, no need to mock any state. Implement your tests as you normally would!