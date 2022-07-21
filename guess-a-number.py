import random
max = int(input("enter max number to guess"))
number_to_guess = random.randint(1,max)
end_of_game = False
mistakes = 1
while not end_of_game:
    
    guess = int(input("guess a number"))
    print(mistakes)
    if guess < number_to_guess:
        print("to small")
        mistakes = mistakes + 1 
 
    elif guess > number_to_guess:
        print("to big")
        mistakes += 1
        
    elif guess == number_to_guess:
        print("Yes!")
        break

    if mistakes == 6:
        print(number_to_guess)
        print("Too many mistakes ;c GG")
        end_of_game = True