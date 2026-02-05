subjects=int(input("Enter the number of subjects:"))
marks=[]
for i in range(subjects):
    while True:
        m=int(input(f"Enter the marks for subject {i+1}: "))
        if 0<=m<=100:
            marks.append(m)
            break
        else:
            print("Plase Enter valid marks(0-100)")
print("Marks obtained for each subject:",marks)
total_marks=0
for mark in marks:
    total_marks+=mark
average_marks=total_marks/len(marks)
print("Total marks obtained:",total_marks)
print("Average Marks:",average_marks)
if average_marks>=75:
    print("Grade:A")
elif average_marks>=60:
    print("Grade:B")
elif average_marks>=40:
    print("Grade:C")
else:
    print("Grade:F")
if average_marks>=40:
    print("Congratulations! You have successfully passed the examination")
else:
    print("You have failed the examination")
print("Maxmum Marks obtained:",max(marks))
print("Minimum marks obtained:",min(marks))
