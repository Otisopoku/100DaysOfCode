import sys
import os 
import time
from menu import MENU
resources = {
    "water": 20000,
    "milk": 20000,
    "coffee": 20000,
    "money": 200
}

def clear_console():
    time.sleep(3) # sleep 3 seconds to display a message to the current buyer then clear console
    os.system("cls" if os.name == "nt" else "clear")

def has_sufficient_resources(order_choice: str) -> tuple:
    global resources

    ingredients = MENU[order_choice]["ingredients"]
    for item, required_amount in ingredients.items():
        if resources[item] < required_amount:
            return (False,item)
    return (True,item)

def is_sufficient_money(money: float, order_choice: str) -> bool:
    return money >= MENU[order_choice]["cost"]

def compute_money(money: dict) -> float:
    '''computes the money of the buyer'''
    QUARTER_CONVERT = 0.25
    DIME_CONVERT = 0.1
    NICKLE_CONVERT = 0.05
    PENNY_CONVERT = 0.01
    total_sum = (money["quarters"] * QUARTER_CONVERT)  + (money["dimes"] * DIME_CONVERT)+ (money["nickles"] * NICKLE_CONVERT )+ (money["pennies"] * PENNY_CONVERT)
    return total_sum

def user_balance(money_sum: float, user_choice: str):
    '''returns the balance of the user'''
    return money_sum - MENU[user_choice]["cost"]

def update_resources(user_choice: str) -> bool:

    '''updates resources and adds to profit'''
    if user_choice == "espresso":
        resources["water"] -= MENU[user_choice]["ingredients"]["water"]
        resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[user_choice]["ingredients"]["water"]
        resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
        resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
    resources["money"] += MENU[user_choice]["cost"]

def show_report() -> str:
    global resources
    return (
        f'''
Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${resources["money"]:.2f}
'''
    )

while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "report":
        print(show_report())
        clear_console()
    elif user_choice == "off":
        sys.exit()
    else:
        '''
        1. check your resources based on the user choice
        2. check if user has sufficient money
        3. make deductions from resources and add profit
        4. give user balance
        5. Prepare the user whatever he likes!
        '''
        check_resources:tuple = has_sufficient_resources(user_choice)
        if check_resources[0]:
            num_quarters = int(input("Enter the number of quaters: "))
            num_dimes = int(input("Enter the number of dimes: "))
            num_nickles = int(input("Enter the number of nickles: "))
            num_pennies = int(input("Enter the number of pennies: "))
            total_money = compute_money({"quarters": num_quarters, "dimes": num_dimes, "nickles": num_dimes, "pennies": num_pennies})
            check_user_money = is_sufficient_money(total_money, user_choice)
            if check_user_money:
                update_resources(user_choice)
                balance = user_balance(total_money, user_choice)
                if balance:
                    print(f"Here is ${balance:.2f} dollars in change")
                print(f"Here is your {user_choice}. Enjoy!")
                clear_console()
            else:
                print("Not sufficient funds to make this order")
                clear_console()
        else:
            print(f"Sorry, there is not enough {check_resources[1]}.")
            clear_console()

'''
AI code, more modular

import sys
import os
import time
from menu import MENU

# Initial resources
resources = {
    "water": 20000,
    "milk": 20000,
    "coffee": 20000,
    "money": 200
}

def clear_console(delay: int = 3):
    """Pause for a few seconds, then clear the console."""
    time.sleep(delay)
    os.system("cls" if os.name == "nt" else "clear")

def has_sufficient_resources(order_choice: str) -> tuple[bool, list]:
    """
    Check if there are enough resources for the chosen drink.
    Returns (True, []) if sufficient, otherwise (False, [missing_items]).
    """
    missing_items = []
    ingredients = MENU[order_choice]["ingredients"]

    for item, required_amount in ingredients.items():
        if resources.get(item, 0) < required_amount:
            missing_items.append(item)

    return (len(missing_items) == 0, missing_items)

def is_sufficient_money(money: float, order_choice: str) -> bool:
    """Check if the user has inserted enough money."""
    return money >= MENU[order_choice]["cost"]

def compute_money(money: dict) -> float:
    """Compute the total amount inserted by the user."""
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    return sum(money[coin] * COIN_VALUES[coin] for coin in COIN_VALUES)

def user_balance(money_sum: float, user_choice: str) -> float:
    """Calculate the change to return to the user."""
    return round(money_sum - MENU[user_choice]["cost"], 2)

def update_resources(user_choice: str):
    """Deduct used ingredients and add profit."""
    for item, amount in MENU[user_choice]["ingredients"].items():
        resources[item] -= amount
    resources["money"] += MENU[user_choice]["cost"]

def show_report() -> str:
    """Return a formatted string of current resources."""
    return (
        f"Water: {resources['water']}ml\n"
        f"Milk: {resources['milk']}ml\n"
        f"Coffee: {resources['coffee']}g\n"
        f"Money: ${resources['money']:.2f}\n"
    )

def process_order(user_choice: str):
    """Handle the full order process."""
    # 1. Check resources
    sufficient, missing = has_sufficient_resources(user_choice)
    if not sufficient:
        print(f"Sorry, there is not enough: {', '.join(missing)}.")
        clear_console()
        return

    # 2. Get coins from user
    try:
        num_quarters = int(input("Enter the number of quarters: "))
        num_dimes = int(input("Enter the number of dimes: "))
        num_nickles = int(input("Enter the number of nickles: "))
        num_pennies = int(input("Enter the number of pennies: "))
    except ValueError:
        print("Invalid input. Please enter whole numbers for coins.")
        clear_console()
        return

    total_money = compute_money({
        "quarters": num_quarters,
        "dimes": num_dimes,
        "nickles": num_nickles,
        "pennies": num_pennies
    })

    # 3. Check if enough money
    if not is_sufficient_money(total_money, user_choice):
        print("Not sufficient funds to make this order.")
        clear_console()
        return

    # 4. Update resources and give change
    update_resources(user_choice)
    balance = user_balance(total_money, user_choice)
    if balance > 0:
        print(f"Here is ${balance:.2f} in change.")
    print(f"Here is your {user_choice}. Enjoy!")
    clear_console()

# Main loop
while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

    if user_choice == "report":
        print(show_report())
        clear_console()
    elif user_choice == "off":
        sys.exit()
    elif user_choice in MENU:
        process_order(user_choice)
    else:
        print("Invalid choice. Please select espresso, latte, or cappuccino.")
        clear_console()

'''