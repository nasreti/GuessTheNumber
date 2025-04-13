#2025-04-12
# High and Low number guessing game. between 1-100

import random


#random number gen.
random_num = random.randint(1, 100)
ui = 0
guesses = 0
while random_num != ui:
    ui = int(input("give me your best guess: "))
    if ui < random_num:
        print("Higher!")
        guesses = guesses + 1        
    elif ui > random_num:
        print("Lower!")
        guesses = guesses + 1
        

    if ui == 6969:
        print(f"cheat table:hehe the number is {random_num} guess it and have fun Hehe")

print(f"CONGRATS U GOT IT it took you {guesses + 1} guesses")