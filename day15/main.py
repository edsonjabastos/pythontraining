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
    while user_input not in valid_input:
        print("Invalid input, please type again.")
        user_input = input("What would you like? (espresso/latte/cappuccino):")
    print("Line 76")
    return user_input


def receive_payment():
    print("Please insert coins")
    quantities_of_each_coin = []
    loop_counter = 0
    total_money = 0
    for key in coins:
        coins_units = 0
        try:
            coins_units = int(input(f"How many {key}: "))
            print(coins_units)
        except ValueError:
            # while type(coins_units) != int and coins_units >= 0:
            #     print('error: only positive numbers will be accepted')
            #     coins_units = int(input(f"How many {key}: "))
            print('invalid input')
        # coins_units = int(input(f"How many {key}: "))
        # while type(coins_units) != int:
        #     print(f"{key} quantity invalid")
        #     coins_units = int(input(f"How many {key}: "))
        quantities_of_each_coin.append(coins_units)
        total_money += (coins[key] * quantities_of_each_coin[loop_counter])
        loop_counter += 1
    return total_money


def make_coffee_and_deliver(coffee_type):
    coffee_type_ingredients = MENU[coffee_type]['ingredients']
    for key in coffee_type_ingredients:
        resources[key] = resources[key] - coffee_type_ingredients[key]
        print(resources)
        print(key)
    print(f"Here is your {coffee_type}")


def check_payment(user_money, item_price):
    payment_ok = False
    if user_money >= cost:
        payment_ok = True
        resources["money"] += cost
        change = user_money - item_price
        print(f"Here is ${change:.3g} in change.")
    else:
        print(f"Sorry that's not enough money. Money refunded.\n"
              f"You got {user_money}, are missing {item_price - user_money}")
    return payment_ok


def check_resources_is_ok(order, current_resources):
    order_ingredients = order['ingredients']
    print(order_ingredients)
    what_is_missing = []
    item = 0
    print(order_ingredients)
    for key in order_ingredients:
        print(key)
        print(current_resources[key])
        print(order_ingredients[key])
        if current_resources[key] < order_ingredients[key]:
            what_is_missing.append(key)
            print(f"Sorry there is not enough {what_is_missing[item]}.")
            print(current_resources)
            item += 1
            print("não foi")
    print("foi")
    print(len(what_is_missing))
    return len(what_is_missing) == 0


while coffee_machine_is_on:
    user_action = user_inputer_checker()
    print(f"Line 117, {user_action}")
    if user_action == 'off':
        coffee_machine_is_on = user_commands[user_action](coffee_machine_is_on)
    elif user_action == 'report':
        user_commands[user_action]()
    elif user_action == 'espresso':
        cost = MENU[user_action]['cost']
        resources_is_ok = check_resources_is_ok(MENU[user_action], resources)
        print("Line 126", cost)
        if resources_is_ok:
            money_added = receive_payment()
            print("Line 124", money_added)
            payment_is_ok = check_payment(money_added, cost)
            if payment_is_ok:
                print("Line 128", payment_is_ok)
                make_coffee_and_deliver(user_action)
    elif user_action == 'latte':
        cost = MENU[user_action]['cost']
        resources_is_ok = check_resources_is_ok(MENU[user_action], resources)
        print("Line 126", cost)
        if resources_is_ok:
            money_added = receive_payment()
            print("Line 124", money_added)
            payment_is_ok = check_payment(money_added, cost)
            if payment_is_ok:
                print("Line 128", payment_is_ok)
                make_coffee_and_deliver(user_action)
    elif user_action == 'cappuccino':
        cost = MENU[user_action]['cost']
        resources_is_ok = check_resources_is_ok(MENU[user_action], resources)
        print("Line 126", cost)
        if resources_is_ok:
            money_added = receive_payment()
            print("Line 124", money_added)
            payment_is_ok = check_payment(money_added, cost)
            if payment_is_ok:
                print("Line 128", payment_is_ok)
                make_coffee_and_deliver(user_action)
    print(resources)
