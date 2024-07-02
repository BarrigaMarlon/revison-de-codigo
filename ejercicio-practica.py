import random 

def guess_the_number():
    number_to_guess = random.randint(1, 100) 
    attempts = 0
    guessed = False

    print("Welconme to the number Guessing Game")
    print("i have selected a numbet between 1 and 100. try to guss it.")

    while not guessed:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("too low! try again,")
        elif user_guess > number_to_guess:
            print("too high! try again.")
        else:
            guessed = True
            print(f"congratulations! you guessed the number in {attempts} attempts.")

# example usage 
guess_the_number()
        