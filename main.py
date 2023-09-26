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

income = 0
is_on = True


def is_resource_sufficient():
    drink = MENU[customer_order]

    for resource in drink["ingredients"]:
        if drink["ingredients"][resource] >= resources[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True


def finalize_transaction(paid):
    drink = MENU[customer_order]

    for resource in drink["ingredients"]:
        resources[resource] -= drink["ingredients"][resource]

    change_due = paid - drink["cost"]
    global income
    income += drink["cost"]
    print(f"Here is ${change_due} in change.")
    print(f"Here is your {customer_order}. Enjoy!")
    return True


while is_on:
    customer_order = input("What would you like? (espresso/latte/cappuccino): ")
    if customer_order == "off":
        is_on = False
    elif customer_order == "report":
        print(resources)
        print(income)
    else:
        if is_resource_sufficient():
            payment = {
                "pennies": float(input("How many pennies?\n")),
                "nickles": float(input("How many nickles?\n")),
                "dimes": float(input("How many dimes?\n")),
                "quarters": float(input("How many quarters?\n"))
            }
            total_paid = sum(
                .01 * count if tender == "pennies" else
                .05 * count if tender == "nickles" else
                .10 * count if tender == "dimes" else
                .25 * count if tender == "quarters" else
                0
                for tender, count in payment.items()
            )
            total_paid = round(total_paid, 2)
            beverage = MENU[customer_order]
            if total_paid <= beverage["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                finalize_transaction(total_paid)


# TODO: 1. Print report of all coffee machine resources

# TODO: 2. Check resources sufficient to make drink order

print("test")