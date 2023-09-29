import validators

def main():
    email = input('What is your email address? '.strip())
    print('Valid') if validators.email(email) == True else print('Invalid')

if __name__ == '__main__':
    main()