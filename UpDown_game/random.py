import random

random_float = pythonProject.Project.UpDown_game.random()
print(random_float)

love_score = random.randint(1, 100)
print(f"your love score {love_score}")

up = 0
down = 0
print("up down game lets go")
print(input("what do you want up and down choice your self\n"))
user_up=str(up)
user_down=str(down)

random_float = random.randint(0, 1)
if user_up == 0:
    print(f"u are win {user_up}\n")
else:
    print(f"u are lose {user_down}")
