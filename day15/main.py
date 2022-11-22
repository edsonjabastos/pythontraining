MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# TODO 1: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
coffee_machine_is_on = True


def espresso():
    return


def latte():
    return


def cappuccino():
    return


def report():
    print(f" - Water: {resources['water']}ml\n"
          f" - Milk: {resources['milk']}ml\n"
          f" - Coffee: {resources['coffee']}g\n"
          f" - Money: ${resources['money']}")


def off(machine):
    machine = False
    return machine


user_commands = {
    'expresso': espresso,
    'latte': latte,
    'cappuccino': cappuccino,
    'report': report,
    'off': off
}

coins = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickles': 0.05,
    'pennies': 0.01
}


def user_inputer_checker():
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    valid_input = ['espresso', 'latte', 'cappuccino', 'report', 'off']
    print(f"Line 73, {user_input}")
    if user_input not in valid_input:
        print("Invalid input, please type again.")
        user_inputer_checker()
    print("Line 76")
    return user_input


def receive_payment():
    print("Please insert coins")
    coins_units = []
    loop_counter = 0
    total_money = 0
    for key in coins:
        coins_units.append(int(input(f"How many {key}: ")))
        total_money += (coins[key] * coins_units[loop_counter])
        loop_counter += 1
    return total_money


def deliver_coffee(coffee_type):
    print(f"Here is your {coffee_type}")


def check_payment(user_money, item_price):
    payment_ok = False
    if user_money >= cost:
        payment_ok = True
        resources["money"] += user_money
        print(f"Here is ${user_money - item_price} in change.")
    else:
        print(f"Sorry that's not enough money. Money refunded.\n"
              f"You got {user_money}, are missing {item_price - user_money}")
    return payment_ok


def resources_checker(order, current_resources):
    print


while coffee_machine_is_on:
    user_action = user_inputer_checker()
    print(f"Line 117, {user_action}")
    if user_action == 'off':
        coffee_machine_is_on = user_commands[user_action](coffee_machine_is_on)
    elif user_action == 'report':
        user_commands[user_action]()
    elif user_action == 'espresso':
        money_added = receive_payment()
        print("Line 124", money_added)
        cost = MENU[user_action]['cost']
        print("Line 126", cost)
        payment_is_ok = check_payment(money_added, cost)
        print("Line 128", payment_is_ok)
