n=int(input("Enter number: "))
temp = n
sum = 0
while(n>0):
    r = n%10
    sum += r*r*r
    n = n//10
if sum == temp:
    print("Armstrong number.")
else:
    print("Not Armstrong!!!")