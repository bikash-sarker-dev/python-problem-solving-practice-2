# Problem 1: Student Grade Calculator

student_name = input("Enter the student name : ")

bangla = int(input("this is bangla subject number: " ))
english = int(input("this is english subject number: " ))
ict = int(input("this is ict subject number: " ))

total_Mark = bangla + english + ict

average = total_Mark / 3

if average >= 80:
    grade = "A+"
elif average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"



print(f"Student Name: {student_name}")
print(f"Total Marks: {total_Mark}")
print(f"Average: {round(average, 2)}")
print(f"Grade: {grade}")


