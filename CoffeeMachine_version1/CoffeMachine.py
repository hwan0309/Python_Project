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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
       if order_ingredients[item] >= resources[item]:
        print(f"물이 충분하지 않습니다.{item}.")
        return False
    return True

def process_coins():
    print("please insert coins")
    total = int( input("how many 500원?"))* 500
    total += int(input("how many 100원?")) * 100
    total += int(input("how many 50원?")) * 50
    total += int(input("how many 10원?")) * 10
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"거스름돈 {change}원")
        global profit
        profit += drink_cost
        return True
    else:
        print("거스름돈이 부족합니다.")
        return False

def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"주문한 {drink_name} 입니다.")

is_on = True

while is_on:
    choice = input("어떤 커피를 원하시나요 (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
       print(f"Water: {resources['water']}ml")
       print(f"Milk: {resources['milk']}ml")
       print(f"Coffee: {resources['coffe']}g")
       print(f"금액 {profit}원")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
           payment = process_coins()
           if is_transaction_successful(payment,drink["cost"]):
               make_coffe(choice, drink["ingredients"])
