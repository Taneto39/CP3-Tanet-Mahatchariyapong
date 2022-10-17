account = {'A': 5000, 'B': 0}


def getAllBalance():
    for i in account:
        print(i, account[i])


def deposit(money):
    if money <= 0:
        raise Exception('Type correct number!!')
    print(f'Deposit {money}฿ to A\'s account.')
    account['A'] += money
    getAllBalance()


def withdraw(money):
    if money <= 0:
        raise Exception('Type correct number!!')
    if money > account['A']:
        raise Exception('Not enough balance!!')
    print(f'Withdraw {money}฿ from A\'s account.')
    account['A'] -= money
    getAllBalance()


def transfer(money):
    if money <= 0:
        raise Exception('Type correct number!!')
    if money > account['A']:
        raise Exception('Not enough balance!!')
    print(f'Transfer {money}฿ from A\'s account to B\'s account.')
    account['A'] -= money
    account['B'] += money
    getAllBalance()


try:
    getAllBalance()
    transfer(5000)
except Exception as e:
    print(e)
