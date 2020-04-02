import random
import string
print("Welcome to password Generator!!")
print("Number of alphabets: ", end =" ")
a = int(input())
print("Number of digits: ", end =" ")
d = int(input())
print("Number of special Characters: ", end =" ")
s = int(input())
if a+d+s >= 6:
    RL = RD = RS = ''
    L = string.ascii_letters
    D = string.digits
    for i in range(a):  
        RL = RL + random.choice(L)
    for i in range(d):  
        RD = RD + random.choice(D)
    for i in range(s):
        RS = RS + random.choice('!$%&()*?@^')
    P = RD + RL + RS 
    P = list(P)
    random.shuffle(P)
    K = ''.join(P)
    print("Generated password is : ", K)
else:
    print("The password should be a minimum of 6 characters long.")