import random

ROWS = 3
COLS = 3

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)


def deposit():
    while True:
        amount = input("what would you like to deposit? $")
        if amount.isdigit(): # it only allows the whole numbers
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to the bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): # it only allows the whole numbers
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter a valid number of lines")
        else:
            print("please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("what would you like to bet? $")
        if amount.isdigit(): # it only allows the whole numbers
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be in between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter a number.")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            print(f"You are betting ${bet} on {lines} lines. TOtal bet is equal to : ${total_bet}")
            break
        else:
            print(f"NOT sufficient balance your balance : ${balance}")
   


main()