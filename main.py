import random

MAX_LINES = 3 #constante
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

#function to get the slot machine spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #loop to get the symbols and the amount of times they appear
        for _ in range(symbol_count): #loop to add the symbols to the list
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols): #generate the columns for every column that we have
        column = []
        current_symbols = all_symbols[:] #creates a copy of the list s
        for _ in range (rows):    
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


##funcion to print the slot machine spin
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate (columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


##funcion to get the amount of money to deposit
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): #check if the number is a integer
            amount = int(amount)
            if amount>0: #check if the number is greater than 0
                break
            else:
                print("Amount must be greater than 0.")
        else: #if it's not a number
            print("Please enter a number.")
    return amount


##funcion to get the number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: #check if the number is between 1 and MAX_LINES
                break
            else:
                print("Enter a valid number of lines.")
        else: 
            print("Please enter a number.")
    return lines  

#function to get the amount of money to bet on each line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): 
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else: 
            print("Please enter a number.")
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet>balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break


    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)


main()



