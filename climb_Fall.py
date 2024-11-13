import random
def dice():
    num = random.randint(1,6)
    return num
# import Dicepgm


print("🚩"*25,"CLIMB FALL...⛳️","🚩"*25)
A = []
B = []
i = 0
while sum(A)!=10 and sum(B)!=10:
    if(sum(A)<10 and i%2==0):
        print("A's Turn:   ")
        if(input()=="p"):
            throw = dice()
            A.append(throw)
            print(sum(A))
        i += 1
    elif(sum(B)<10 and i%2!=0):
        print("B's Turn:   ")
        if(input()=="p"):
            throw = dice()
            B.append(throw)
            print(sum(B))
        i += 1    
    elif (sum(A)>10):
        A.clear()
    elif (sum(B)>10):
        B.clear()
    else:
        print("Winner")
if(sum(A)==10):
    print("A is the Winner...😎")
else:
    print("B is the Winner...😎")
    