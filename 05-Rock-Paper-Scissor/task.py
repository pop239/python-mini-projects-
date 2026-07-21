import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock , paper , scissors]

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if my_choice >= 0 and my_choice <=2:
    print(game[my_choice])

computer_choice=random.randint(0,2)
print("Computer chose:\n")
print(game[computer_choice])

if my_choice == computer_choice:
    print("it's a draw")

elif my_choice == 0:
    if computer_choice == 1:
        print("you lose")
    elif computer_choice == 2:
            print("you win")

elif my_choice == 1:
    if computer_choice == 0:
        print("you win")
    elif computer_choice == 2:
            print("you lose")

elif my_choice == 2:
    if computer_choice == 0:
        print("you lose")
    elif computer_choice == 1:
            print("you win")

else:
    print("invalid choice")







