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

#Write your code below this line 👇
print("Welcome to the WORLD ROCK PAPER SCISSORS game! \n")
image_list = [rock, paper, scissors]
my_choice = int(input("What do you choose? Enter 0 for Rock, 1 for Paper, and 2 for Scissors \n"))
if (my_choice >= 3) or (my_choice < 0):
  print("You lose! You typed invalid number")
else:
  print(image_list[my_choice])
  list_of_attempts = ["rock", "paper", "scissors"]
  
  computer_choice = random.randint(0, len(list_of_attempts) - 1)
  print("Computer chose\n")
  print(image_list[computer_choice])
  
  
  if (my_choice == 0) and (computer_choice == 2):
    print("You win")
  elif (my_choice == 2) and (computer_choice == 1):
    print("You win")
  elif (my_choice == 1) and (computer_choice == 0):
    print("You win")
  elif (my_choice == 2) and (computer_choice == 0):
    print("You lose")
  elif (my_choice == 1) and (computer_choice == 2):
    print("You lose")
  elif (my_choice == 0) and (computer_choice == 1):
    print("You lose")
  elif (my_choice == 0) and (computer_choice == 0):
    print("Draw")
  elif (my_choice == 1) and (computer_choice == 1):
    print("Draw")
  elif (my_choice == 2) and (computer_choice == 2):
    print("Draw")

  

