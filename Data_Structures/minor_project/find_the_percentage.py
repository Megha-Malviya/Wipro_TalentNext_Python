# Data Structure Project 3: Student Marks and Average Calculation

"""You have a record of n students. Each record contains the student's name, and their percent marks in Math, Physics and Chemistry.
The marks can be floating values.You are required to save the record in a dictionary data type.Student’s name is the key. 
Marks stored in a list is the value. The user enters a student's name.
Output the average percentage marks obtained by that student"""


students = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

name = input("Enter a name: ")

if name in students:
    marks = students[name]
    average = sum(marks) / len(marks)
    print(f"Average percentage mark: {average:.0f}")
else:
    print("Student not found!")
