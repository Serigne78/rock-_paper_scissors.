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
user = int(input("What do you? Type 0 for Rock, 1 for paper or 2 for Scissors:\n"))
computer = random.randint(0, 2)
if user == 0 and computer == 1:
      print("ME "+" rock "+
            " Computer  chose: "+ paper+
            " You lose")
if user == 1 and computer == 0:
      print(paper +
            " Computer  chose: "+ rock+
            " You win")
if user == 1 and computer == 2:
      print("Me "+ paper +" Computer chose: "+
      scissors +" You lose"     
      )
if user ==2 and computer ==   1:
      print("Me "+ paper +" Computer chose: "+
      scissors +" You Win")


if user == 0 and computer == 0:
      print("Egality")
if user == 2 and computer ==2:
      print("Egality")
if user == 1 and computer == 1:
      print("Egality")


if user == 0 and computer == 2:
      print("Me "+ rock +" computer choose: " 
      + scissors +" You win" )

if user == 2 and computer == 0:
      print("Me "+ scissors +" computer choose: " 
      + rock +" You loose" )
if user>2:
      print("ERROR")

