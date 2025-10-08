Menu={
    "latte":{
        "ingredients":{
            "water": 150,
            "milk": 100,
            "coffee": 20
        },
        "cost":120
    },
    "espresso":{
        "ingredients":{
            "milk": 60,
            "coffee": 18
        },
        "cost":100
    },
    "cappuccino":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 30
        },
        "cost":200
    }
}
profit=0
resources={
            "water": 500,
            "milk": 300,
            "coffee": 100
}

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    print("Please insert coins...")
    total=0
    coins_five=int(input("How many 5rs coins? : "))
    coins_ten=int(input("How many 10rs coins? : "))
    coins_twenty=int(input("How many 20rs coins? : "))
    total=coins_five*5 + coins_ten*10 + coins_twenty*20
    return total

def is_payment_successful(money_received,coffee_cost):
    if money_received>=coffee_cost:
        global profit
        profit+=coffee_cost
        change=money_received-coffee_cost
        print(f"Here is your {change}rs change")
        return True
    else:
        print("Sorry that's not enough money.Your money refunded")
        return False
    
def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
        resources[item]-= coffee_ingredients[item]
    print(f"Here is your {coffee_name}...Enjoy !!!")

is_on=True
while is_on:
    choice=input("What do you want ? (latte/espresso/cappuccino): ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water={resources['water']}ml")
        print(f"milk={resources['milk']}ml")
        print(f"coffee={resources['coffee']}gm")
    else:
        coffee_type=Menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment=process_coins()
            if is_payment_successful(payment,coffee_type['cost']):
                make_coffee(choice,coffee_type['ingredients'])


