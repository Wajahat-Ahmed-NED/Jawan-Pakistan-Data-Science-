#Assignment 2
# Name : Wajahat Ahmed
eng=78
isl=90
maths=98
totalMarks=300
percentage=(eng+isl+maths)/totalMarks*100
print("Obtained Marks is : ",eng+isl+maths)
print("Total Marks is : ",totalMarks)
print("Percentage is : ",percentage)
if percentage>0 and percentage<100:
    if percentage >= 90:
        print("Your grade is A++")
    elif percentage >= 80:
        print("Your grade is A+")
    elif percentage >= 70:
        print("Your grade is A")
    elif percentage >= 60:
        print("Your grade is B")
    elif percentage >= 50:
        print("Your grade is C")
    elif percentage >= 40:
        print("Your grade is D")
    elif percentage >= 33:
        print("Your grade is E")
    else:
        print("You are Failed")


