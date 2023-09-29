import requests
from sys import argv, exit


def main():
    if len(argv) == 2:
        try:
            number = float(argv[1])
        except:
            exit("Command-line argument is not a number")
    else:
        exit("Missing command-line argument")

    try:
        response = (
            requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        ).json()
    except requests.RequestException:
        exit()

    price_response = float(response["bpi"]["USD"]["rate"].replace(",", ""))
    print(f"${number * price_response:,.4f}")


if __name__ == "__main__":
    main()
