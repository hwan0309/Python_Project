import random

word_list = ["ardvark", "baboon", "camel"]

chose_word = random.choice(word_list)
print(chose_word)
display = []
word_length = len(chose_word)
for _ in range(len(chose_word)):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chose_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
      end_of_game = True
      print("You win")
