import random
import art


def easy_ver(answer):
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
    while attempts!=0:
        guess = int(input("make a guess: "))
        if guess > answer:
            attempts -= 1
            print("too high\n")
            if attempts != 0:
                print("guess again")
                print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess < answer:
            attempts -= 1
            print("too low\n")
            if attempts != 0:
                print("guess again")
                print(f"You have {attempts} attempts remaining to guess the number.")

        else:
            print(f"You got it!  The answer was {answer}.")
            return 0

    print("You've run out of guesses. Refresh the page to run again.")






def hard_ver(answer):
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    while attempts!=0:
        guess = int(input("make a guess: "))
        if guess > answer:
            attempts -= 1
            print("too high\n")
            if attempts != 0:
                print("guess again")
                print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess < answer:
            attempts -= 1
            print("too low\n")
            if attempts != 0:
                print("guess again")
                print(f"You have {attempts} attempts remaining to guess the number.")

        else:
            print(f"You got it!  The answer was {answer}.")
            return 0

    print("You've run out of guesses. Refresh the page to run again.")




def game():

    actual_answer = random.randint(1,100)
    print(art.logo)
    print("""Welcome to the Number Guessing Game!\n 
             I'm thinking of a number between 1 and 100.""")
    print(f"pssst answer is {actual_answer}")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        easy_ver(actual_answer)
    else:
        hard_ver(actual_answer)




game()