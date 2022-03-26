import random

middle_finger = '''
....................../´¯/) 
....................,/¯../ 
.................../..../ 
............./´¯/'...'/´¯¯`·¸ 
........../'/.../..../......./¨¯\ 
........('(...´...´.... ¯~/'...') 
.........\.................'...../ 
..........''...\.......... _.·´ 
............\..............( 
..............\.............\...
'''

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

game_images = [rock, paper, scissors]

humans_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if humans_choice >= 3 or humans_choice < 0:
    print(f"Damn man, You doing it in wrong way\nIdiot! CHOOSE JUST 0, 1 OR 2\n{middle_finger}")
else:
    computer_random_choice = random.randint(0, 2)
    
    print(f"You chose: {humans_choice}\n{game_images[humans_choice]}")

    print(f"Computer random chose: {computer_random_choice}\n{game_images[computer_random_choice]}")

    winner_choices = [[0,2],[1,0],[2,1]]

    match = []

    match.extend([humans_choice, computer_random_choice])

    if match == winner_choices[0] or match == winner_choices[1] or match == winner_choices[2]:
        print("Congrats! You Win!")
    elif match[0] == match[1]:
        print("Same choices! It's a draw!")
    else:
        print("You loose! =/")