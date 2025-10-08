'''
import random
import os
import game_art
import data_info

print(game_art.logo)
score=0
def display_accountinfo(account):
    name=account['name']
    description=account['description']
    country=account['country']
    return f"{name} , a {description} , from {country}"
def check_answer(guess,followers_1,followers_2):
    if followers_1<followers_2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==2:
            return True
        else:
            return False
        
account_2=random.choice(data_info.data)
continue_flag=True
while continue_flag:
    account_1=account_2
    account_2=random.choice(data_info.data)
    while account_1==account_2:
        account_2=random.choice(data_info.data)
    print(f"Compare 1 : {display_accountinfo(account_1)}")
    print(game_art.vs)
    print(f"Compare 2 : {display_accountinfo(account_2)}")
    guess=int(input("Enter ur choice '1' or '2' : "))
    followers_count_1=account_1["follower_count"]
    followers_count_2=account_2["follower_count"]
    is_correct=check_answer(guess,followers_count_1,followers_count_2)
    os.system('cls')
    print(game_art.logo)
    if is_correct==True:
        score+=1
        print(f"You are right.Your score is {score}")
    else:
        print(f"You are wrong.Your final score is {score}")
        continue_flag=False
'''

import random
import os

# Assuming game_art and data_info are custom modules provided elsewhere.
import game_art
import data_info

# Display the game logo
print(game_art.logo)

score = 0

def display_account_info(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

def check_answer(guess, followers_1, followers_2):
    if followers_1 < followers_2:
        return guess == 2
    else:
        return guess == 1

# Start the game with a random account from the data
account_2 = random.choice(data_info.data)
continue_flag = True

while continue_flag:
    account_1 = account_2
    account_2 = random.choice(data_info.data)
    # Ensure account_2 is different from account_1
    while account_1 == account_2:
        account_2 = random.choice(data_info.data)
    
    print(f"Compare 1: {display_account_info(account_1)}")
    print(game_art.vs)
    print(f"Compare 2: {display_account_info(account_2)}")
    
    try:
        guess = int(input("Enter your choice '1' or '2': "))
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")
        continue
    
    followers_count_1 = account_1["follower_count"]
    followers_count_2 = account_2["follower_count"]
    
    is_correct = check_answer(guess, followers_count_1, followers_count_2)
    
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(game_art.logo)
    
    if is_correct:
        score += 1
        print(f"You are right. Your score is {score}.")
    else:
        print(f"You are wrong. Your final score is {score}.")
        continue_flag = False
