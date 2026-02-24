def bank_d(name, balance, bank="SBI"):
    print("Name:", name)
    print("Bank:", bank)
    print("Initial Balance:", balance)

    balance += 2000
    print("Deposited:", 2000)

    balance += 1500
    print("Deposited:", 1500)

    balance -= 1000
    print("Withdrawn:", 1000)

    balance -= 500
    print("Withdrawn:", 500)

    print("Final Balance:", balance)
    print()

bank_d("Vivek", 10000000)
bank_d("Vicky", 15000000, "HDFC")