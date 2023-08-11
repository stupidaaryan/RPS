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

img = [rock, paper, scissors]

user_choice = int(
  input("What would you choose? 0 for Rock, 1 for Paper, 2 for Scissors?\n"))

if user_choice >= 3 or user_choice < 0:
  print("You chose a invalid number so you lose!") 
else:
  print("You chose:-")
  print(img[user_choice])
  
  computer_choice = random.randint(0, 2)
  print("Computer chose:-")
  print(img[computer_choice])
  
  if user_choice == computer_choice:
    print("It's a Draw")
  elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
  elif user_choice == 2 and computer_choice == 0:
    print("You Lose!")
  elif computer_choice > user_choice:
    print("You lose!")
  elif user_choice > computer_choice:
    print("You Win!")
