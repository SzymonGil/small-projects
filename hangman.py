#hangam game, guess the word

import random

hangmans = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_game = False
words = ["ardvark", "baboon", "camel","apple","banana","cat","dog","home","grass","game"]
choice = random.choice(words)
lenght = len(choice)

lives = 6


all = []
for _ in range(lenght):
    all += "_"

while not end_game:
    guess = input("Guess a letter: ").lower()


    for pos in range(lenght):
        letter = choice[pos]
        if letter == guess:
            all[pos] = letter

    if guess not in choice:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose.")

    
    print(f"{' '.join(all)}")

    
    if "_" not in all:
        end_game = True
        print("You win.")

    print(hangmans[lives])
