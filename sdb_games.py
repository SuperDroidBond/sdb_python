import random

def rps_game():

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

    print("Lets Play Rock Paper Scissors!!!\n")

    user_choice1 = int(input("Please chose from the following:\n\n0 For Rock\n\n1 For Paper\n\n2 For Scissors\n\n"))

    random_int = random.randint(0, 2)

    if random_int == 0 and user_choice1 == 0:
        print("\nYou Choose Rock:\n")
        print(rock)
        print("\nComputer Choose Rock:\n")
        print(rock)
        print("\nMatch is Draw\n")
        rps_game()
    elif random_int == 1 and user_choice1 == 0:
        print("\nYou Choose Rock:\n")
        print(rock)
        print("\nComputer Choose Paper:\n")
        print(paper)
        print("\nYou Lost, Computer Won !!!\n")
        rps_game()
    elif random_int == 2 and user_choice1 == 0:
        print("\nYou Choose Rock:\n")
        print(rock)
        print("\nComputer Choose Scissors:\n")
        print(scissors)
        print("\nComputer Lost, You Won !!!\n")
    elif random_int == 0 and user_choice1 == 1:
        print("\nYou Choose Paper:\n")
        print(rock)
        print("\nComputer Choose Rock:\n")
        print(paper)
        print("\nComputer Lost, You Won !!!\n")
    elif random_int == 0 and user_choice1 == 2:
        print("\nYou Choose Scissors:\n")
        print(rock)
        print("\nComputer Choose Rock:\n")
        print(scissors)
        print("\nYou Lost, Computer Won !!!\n")
        rps_game()
    elif random_int == 1 and user_choice1 == 1:
        print("\nYou Choose Paper:\n")
        print(paper)
        print("\nComputer Choose Paper:\n")
        print(paper)
        print("\nMatch is Draw\n")
        rps_game()
    elif random_int == 2 and user_choice1 == 2:
        print("\nYou Choose Scissors:\n")
        print(scissors)
        print("\nComputer Choose Scissors:\n")
        print(scissors)
        print("\nMatch is Draw\n")
        rps_game()
    else:
        print("\nEnter Only the numbers directed.\n\nShow us at least 1 sign of evolution")

def toss_game():
    user_choice2 = input("\nSelect :\n\nHeads\n\nTails\n\n").lower()

    random_int = random.randint(0, 1)

    if random_int == 0:
        print("\nHeads\n")
    else:
        print("\nTails\n")

    if user_choice2 == "heads" and random_int == 0:
        print("You Won\n")
    elif user_choice2 == "tails" and random_int == 1:
        print("You Won\n")
    else:
        print("You Lost")
        toss_game()

print('Hi ! I\'m Jarvis. May I have your name ?')
name = input('\nEnter Your Name \n')
print(f'\nWelcome To SDB Games {name}')
print("\nAre You Ready To Play Games with me ?\n")
user_choice = input("Enter:\n\nY for Yes\n\nN for No\n\n").lower()

if user_choice == "y":
   game_name = int(input(f"\nWhich Game Would You Like To Play {name}:\n\n0 for Toss Game\n\n1 for Rock Paper Scissors\n\nAny Other Number to Exit Games\n\n"))
   if game_name == 0:
       toss_game()
   elif game_name == 1:
       rps_game()
   else:
       exit()
else:
    print(f'Seems you\'re already scared of my name {name} !\n Anyway, GoodBye for Now !!!')
    exit()

