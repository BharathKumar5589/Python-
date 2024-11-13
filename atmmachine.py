

# i/p: Enter the amount to withdraw: 3760 

# O/P:
# 500 INR:  7 notes
# 200 INR:  1 notes
# 100 INR: 0 notes
# 50 INR:  1 notes
# 20 INR: 0 notes
# 10 INR: 1 notes
# 5 INR: notes
# 2 INR: notes
# 1 INR: notes

amount = int(input("Enter amount: "))
no_notes = []
currency = [500,200,100,50,20,10,5,2,1]
for i in currency:
    count = amount//i
    no_notes.append(count)
    print(i,": INR ",count,"notes")
    # amount = amount - i*count
    amount = amount%i
print("Minimum No of notes are: ",sum(no_notes))
    
    
