import random   

chances = 1
number = random.randint(1, 10)
guess = int(input("Guess a Number from 1-9 : "))

while chances < 5 :
    chances += 1
    if guess == number:
        print('Congradulations YOU WON!!!')
        break
    else :
        print('Wrong Guess Again')
        guess = int(input("Guess a Number from 1-9 : "))
        


if chances == 5 and not guess == number :
    print('YOU LOSE!!! The Correct Number is : ', number)