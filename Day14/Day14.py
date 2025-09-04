# Building a simple celebrities comparison game

import celebrities
import random
import os
import time



score = 0

def clear_console():
    os.system("cls" if os.name == "nt" else "clear") 

def compare_celebs(first_celeb, second_celeb):
    return first_celeb["follower_count"] > second_celeb["follower_count"]

def result_from_comparison(first_celeb, second_celeb) -> bool:
    result = compare_celebs(first_celeb, second_celeb)
    global score
    if result:
        score += 1
        print(f"You are right. Current score: {score}")
        return True
    else:
        print(f"You lose, final score is {score}")
        return False


while True:

    clear_console()
    first_celeb = random.choice(celebrities.celebrities)
    second_celeb = random.choice(celebrities.celebrities)

    while second_celeb["name"] == first_celeb["name"]:
        second_celeb = random.choice(celebrities.celebrities)

    print(f"Compare A: {first_celeb["name"]}, a {first_celeb["description"]}, from {first_celeb["country"]}.")
    print(f"Against B: {second_celeb["name"]}, a {second_celeb["description"]}, from {second_celeb["country"]}")

    choice = input("Who has more followers? Type 'A' or 'B': ")

    if choice == 'A':
        result = result_from_comparison(first_celeb, second_celeb)

        if not result:
            break
        
    else:
        result = result_from_comparison(second_celeb, first_celeb)
        if not result:
            break
    time.sleep(5)
    clear_console()

