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

# Set value of coins
quarter = 0.25
dime = 0.10
nickel = 0.05
pennie = 0.01

coins_in_machine = 0
money_to_be_returned = 0


# TODO: 4. Take resources depending of type of coffee selected.
def update_resources(user_prompt):
    resources["water"] = resources["water"] - MENU[user_prompt]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[user_prompt]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[user_prompt]["ingredients"]["coffee"]


# TODO: 1. Print report of coffee machine resources
user_prompt = input("What would you like? (espresso/latte/cappuccino): ")
if user_prompt == "report":
    for resource in resources:
        if resource != "coffee":
            print(f"{resource}: {resources[resource]}ml")
        else:
            print(f"{resource}: {resources[resource]}g")
    print(f"Money: ${coins_in_machine}")

# TODO: 2. Insert Coins into machine and calculate total value of coins
quarters = int(input("How many quarters?: ")) * quarter
dimes = int(input("How many dimes?: ")) * dime
nickels = int(input("How many nickels?: ")) * nickel
pennies = int(input("How many pennies?: ")) * pennie
total_coins = quarters + dimes + nickels + pennies
cost_of_coffee = MENU[user_prompt]['cost']


# TODO: 3. Check if coins inserted are enough to pay for coffee, if yes take the money.
if total_coins >= cost_of_coffee:
    coins_in_machine += cost_of_coffee
    money_to_be_returned += total_coins - cost_of_coffee
    print("Here is your coffee, Enjoy it!")
elif total_coins < cost_of_coffee:
    print("Not enough coins were inserted.")
else:
    print("Error")

update_resources(user_prompt)
print(resources)
print(f"Amount inserted ${total_coins}")
print(f"Amount to be return ${money_to_be_returned}")
print(f"Amount to be charged ${coins_in_machine}")
