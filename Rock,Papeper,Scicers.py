from math import trunc
import os,random
os.system('cls')

possible_choices = ["r","p","s"]



User_score = 0
ai_Score = 0

i = 0

while i < 5:

    user_choice = input("Enter your choice  \n1.Rock(R)\n2.Paper(P)\n3.Scicers(S) :").lower()
    if user_choice in possible_choices:
        
        ai_choice = random.choice(possible_choices)

        print(f'\nAI choice is {ai_choice} and User choice is {user_choice}')
        
        if user_choice == ai_choice :
            print("Tie")
            
        elif user_choice == "r" and ai_choice == "s":
            print("User + 1!")
            User_score += 1
        
        elif user_choice == "s" and ai_choice == "p":
            print("User + 1!")
            User_score += 1

        elif user_choice == "p" and ai_choice == "r":
            print("User + 1!")
            User_score += 1

        else:
            print("AI + 1")
            ai_Score += 1

        print(f'your score is {User_score} and Ai score is {ai_Score}')

        print('\n',15 * "-",'\n')        
    else:
        print("invalid Choice")
        i -= 1
    i += 1

if User_score > ai_Score :
    print(f'You Win . your score is {User_score} and Ai score is {ai_Score}')

else:
    print(f'You Lost. your score is {User_score} and Ai score is {ai_Score}')

