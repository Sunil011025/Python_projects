import random

rock = '''
     _ _ _ _
----'  _ _ _)
       (_ _ _)
      (_ _ _ _)
       (_ _ _)
---- . _(_ _)
     
'''
paper = '''

     _ _ _ _
----' _ _ _ _ _ ) _
      _ _ _ _ _ _ _)
      _ _ _ _ _ _ _ _)
           _ _ _ __)
---- . _ _ _ _ _)
     

'''
scissor = '''
     _ _ _ _
----' _ _ _ _) _ _ 
      _ _ _ _ _ _ _)
      _ _ _ _ _ _ _ _)
        (_ _ _)
---- . _(_ _)
     
'''
game_image = [rock,paper,scissor]
print(" '0' for rock , '1' for paper , '2' for scissor ")
user_choice = int(input("Enter ur choice : "))
if user_choice >= 3 or user_choice <0 :
    print("You entered invalid number !! You lose")
else :
    print(game_image[user_choice])
    computer_choice = random.randint(0,2)
    print("computer_choice : ")
    print(game_image[computer_choice])
    if user_choice == computer_choice :
        print("It's draw ")
    elif computer_choice == 0 and user_choice ==2 :
        print("You lose")
    elif computer_choice == 2 and user_choice ==0 :
        print("You win")
    elif computer_choice > user_choice :
        print("You lose")
    elif computer_choice < user_choice :
        print("You win")