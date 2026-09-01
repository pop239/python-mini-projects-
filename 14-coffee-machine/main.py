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
}



def check_resources_sufficient(order_ing):
    for item in order_ing:
        if order_ing[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():

    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction(money_received,cost_drink):
    if money_received >= cost_drink:
        change = round(money_received - cost_drink, 2)
        global profit
        profit += cost_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ing):
    for item in order_ing:
        resources[item] -= order_ing[item]
        print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True
while is_on:

    choose = input("What would you like? (espresso/latte/cappuccino)")
    if choose == "off":
        is_on = False
    elif choose == "report":
        print(f"Water:{resources["water"]}lm")
        print(f"Milk: {resources["milk"]}lm")
        print(f"Coffee: {resources["coffee"]}")
        print(f"Money: {profit}")

    else:
        drink = MENU[choose]
        if check_resources_sufficient(drink["ingredients"]):
         pay = process_coins()
        if transaction(pay , drink["cost"]):
            make_coffee(choose , drink["ingredients"])
















