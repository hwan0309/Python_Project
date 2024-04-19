import random
from pythonProject.Project.Vs_game.game_data import data
from pythonProject.Project.Vs_game.game_art import logo
from pythonProject.Project.Vs_game.game_art import vs


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a{account_descr}, from{account_country}")

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers and guess == "a":
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = random.choice(data)
    account_b = random.choice(data)

    print(account_b)
    print(account_a)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("누가 팔로우가 제일 많을까 'A' or 'B' :").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #clear()

    if is_correct:
        score += 1
        print(f"정답! score: {score}.")
    else:
        game_should_continue = False
        print(f"땡! score: {score}.")

