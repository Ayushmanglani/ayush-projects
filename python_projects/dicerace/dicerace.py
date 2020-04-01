import random

def play():
    dice1 = [1,2,3,4,5,6]
    r = random.choice(dice1)
    return r 
if __name__ == '__main__':
    
    print("Enter Player 1 Name:")
    X = input()
    print("Enter Player 2 Name:")
    Y = input()
    print("Enter finishing Score")
    N = int(input())
    b = random.randint(0,100)
    a = random.randrange(0,101,1)
    k = 0
    A = B = 0
    print("Start? Y/N")
    r = input().upper()
    if r == 'Y':
        while k == 0:
            b = random.randint(0,100)
            a = random.randrange(0,101,1)
            if a > b:
                print("Its"+" "+ X +"'s Turn")
                z = play()
                A = A + z
                print(X + " got: "+ str(z))
            else:
                print("Its"+" "+ Y +"'s Turn")
                z = play()
                B = B + z
                print(Y + " got: "+ str(z))
            print(X +" : "+ str(A))
            print(Y +" : "+ str(B))
            if A >= N or B >= N:
                print("Game Over")
                if A > B:
                    print("--- "+X+" Won ---")
                elif B>A:
                    print("--- "+Y+" Won ---")
                elif A==B:
                    print("Game Drawn")
                k = 1
                break
            print("Next Move? Y/N")
            z = input().upper()
            if z == 'N':
                k = 1
                print("Thanks for Playing")
    else:
        print("No Problem! Thanks for Joining")
            