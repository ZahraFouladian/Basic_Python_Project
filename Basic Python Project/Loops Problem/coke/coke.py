def main():
    total_coin = 0
    cost = 50
    while total_coin < 50:
        print(f"Amount Due: {cost - total_coin}")
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            total_coin = coin + total_coin
    print(f"Change Owed: {total_coin - cost}\n")

if __name__ == "__main__":
    main()
