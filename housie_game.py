import random
print("*"*25,"Housie Game","*"*25)
l = []
flag = True
while (input("Enter P to play and E to Exit : ")=="P"):
    num = random.randint(1,5)
    while(num in l):
        num = random.randint(1,5)
        if(len(l)==5):
            flag = False
            break
    if flag:
        print(num)
        l.append(num)
    else:
        print("Game Ended!!!")
        break
print(l)
