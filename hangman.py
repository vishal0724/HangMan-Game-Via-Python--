import random

def left_image(left1):  #make function for hangman body
    if left==9:
        print("     -------")
    elif left==8:
        print("     -------")
        print("        !   ")
    elif left==7:
        print("     -------")
        print("        !   ")
        print("        0   ")
    elif left==6:
        print("     -------")
        print("        !   ")
        print("        0   ")
        print("        !   ")
    elif left==5:
        print("     -------")
        print("        !   ")
        print("        0   ")
        print("        !   ")
        print("        !   ")
    elif left==4:
        print("     -------")
        print("        !   ")
        print("        0   ")
        print("        !   ")
        print("        !   ")
        print("       /    ")
    elif left==3:
        print("     -------")
        print("        !   ")
        print("        0   ")
        print("        !   ")
        print("        !   ")
        print("       / \  ")
    elif left==2:
        print("     -------")
        print("        !   ")
        print("        0   ")
        print("       \!   ")
        print("        !   ")
        print("       / \  ")
    elif left==1:
        print("     -------")
        print("        !   ")
        print("        0   ")
        print("       \!/  ")
        print("        !   ")
        print("       / \  ")
    else:
        print("     -------")
        print("        !   ")
        print("        0   ")
        print("       /!\  ")
        print("        !   ")
        print("       / \  ")

name=str(input("Enter Your's name:  "))
print()
print("Walcome   "+name)
print("-------------------------------")
print("""This is Hangman Game.
Guess the word in only 10 chances.""")
print("Guess the word: _ _ _ _ _ ")
print()

random_word=random.choice([ "prove", "pound", "train", "bread", "laugh", "tiger", "faith", "beach", "fancy", 'image', "mount", "shade", "thick" ])

user_letter=str(input("→")) #take first input from user
user_letter=user_letter.lower()
if user_letter not in ("abcdefghijklmnopqrstuvwxyz"):
        user_letter=""

left=9
letter_store=list("-----")
find_index=0
collect=""
wrong_letter=""

while len(user_letter)>0 and len(user_letter)<2:  #start while loop and check the user input any letter or not 

    if user_letter in random_word:  #true letter block-----
        find_index=random_word.index(user_letter) #find index value in random word.
        
        letter_store.insert(find_index, user_letter)
        letter_store.pop(find_index+1)

        print("Wrong letters are: ",wrong_letter," ")
        
        collect=""
        for i in letter_store:
            collect= collect+i
        print('Guess  the letter: ',collect)
        if collect==random_word:
            print("You win the game.")
            break

    else:                    # wrong letter block---
        if left==0:
            print("You loss, Hangman killed.")
            left_image(left)
            print("Paly Again!!")
            break

        else:
            print()
            print(left," turns are left")
            left_image(left)
            wrong_letter=wrong_letter+" "+user_letter
            print("Wrong letters are: ",wrong_letter)
            print('Guess  the letter: ',collect)
        left-=1  # decrease the left chance.

    user_letter=str(input("→"))  # take input in loop  and convert----
    user_letter=user_letter.lower()
    if user_letter not in ("abcdefghijklmnopqrstuvwxyz"):
        print("Press some invalid keys")
        break
    

else:
    print("You press more than one key. Or press some invalid keys")