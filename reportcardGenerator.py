def grade(score):
    if(score>=90):
        grade = "A"
    elif (score>=80 and score<=89):
        grade = "B"
    elif (score>=70 and score<=79):
        grade = "C"
    elif (score>=60 and score<=69):
        grade = "D"
    else:
        grade = "F" 
    return grade

def report(name):
    l = ["Telugu","hindi","English","maths","science","social"]
    marks = []
    for i in l:
        print("enter",i, "Marks: ")
        m = float(input())
        marks.append(m)
    average = sum(marks)/len(marks) 
    print("*"*20,"\tREPORT CARD\t","*"*20)
    print("Student Name: ",name)
    # no_of_subjects = len(l)
    for i in range(len(l)):
        subject_grade = grade(marks[i]) 
        print(l[i]," : ",marks[i],"Grade :",subject_grade)
    total_marks = sum(marks)
    print("Total Marks: ",total_marks)
    print("Average Score : {:.2f}".format(average))
    total_score = total_marks/len(l)
    final_grade = grade(total_score)
    print("Final Grade : ",final_grade)
    
name = input("Enter name: ")
report(name)
