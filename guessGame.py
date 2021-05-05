import random 

chances = 1
number = random(1, 10)
guess = int(input("Guess a Number from 1-9 : "))

while chances < 5   
    if guess == number:
    print('Congradulations YOU WON!!!')
    else :
        print('Wrong Guess Again')
        guess = int(input("Guess a Number from 1-9 : "))
        chances += 1
    break

if not chances < 5:
    print('YOU LOSE!!! The Correct Number is : ', number)