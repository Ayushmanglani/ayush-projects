'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import random

r = random.randint(1,21)
print("Guess the number choosen by System")
x = int(input())
k = 0
while k==0:
    if x == r:
        print("Wow! You Chose the Correct Number")
        k = 1
    else:
        if x<r:
            print("Your Answer is too low! Want to try again? Y/N")
            a = input()
            if a == 'N':
                k = 1
                print("System Guessed: " + str(r))
            elif a == 'Y':
                print("Great! Choose a new number")
                x = int(input())
            else:
                print("Sorry! Invalid Input")
             
        if x>r:
            print("Your Answer is too High! Want to try again? Y/N")
            a = input()
            if a == 'N':
                k = 1
                print("System Guessed: " + str(r))    
            elif a == 'Y':
                print("Great! Choose a new number")
                x = int(input())
            else:
                print("Sorry! Invalid Input")