import json
from student import Student


def save_students(students):
    student_data=[]

    for student in students: 
        student_data.append(student.to_dict())
    with open("students.json", "w")as file:
        json.dump(student_data, file, indent=4)


def load_students():
    try:

        with open("students.json", "r")as file:
            data = json.load(file)
            students = []

        for student in data:
            students.append(
                Student(
                    student["name"],
                    student["roll"],
                    student["english"],
                    student["math"],
                    student["science"]
                )
            )

        return students

    except FileNotFoundError:
        return []
        
    


students = load_students()

while True:
    print("\n==== Student Result Management ====")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = int(input("Enter your choice :"))

    if choice == 1:
        name = input("Enter Name: ")
        roll = int(input("Enter Roll: "))
        english = int(input("Enter english marks: "))
        math = int(input("Enter math marks: "))
        science = int(input("Enter science marks: "))

        student1 = Student(name, roll, english, math, science)
        students.append(student1)
        save_students(students)
        print("Students added successfully! ")

    elif choice == 2:
        if not students:
            print("no students found ")
        else:
            
            for student in students:
                student.display_student()
    elif choice == 3:
        search_roll = int(input("Enter Roll Number: "))
        found = False
        for student in students:
            if student.roll == search_roll:
            
                student.display_student()
                found = True
                break 
            
        if not found:
            print("Student not found:")        

    elif choice == 4:
        delete_roll = int(input("Enter Roll number:"))
        found = False

        for student in students:
            if student.roll == delete_roll:

                students.remove(student)
                save_students(students)
                print("Student deleted successfully!")
                found = True
                break
            
        if not found:
            print("Student not found: ")
            

    elif choice == 5:
        update_roll = int(input("Enter Roll number:"))
        found = False

        for student in students:
            if student.roll == update_roll:
                student.english = int(input("Enter new English Marks: "))
                student.math = int(input("Enter new Math Marks: "))
                student.science = int(input("Enter new Science Marks: "))
                save_students(students)
                print("Student Marks Updated Successfully! ")
                student.display_student()
                found = True
                break

        if not found:   
            print ("Student not found") 

    elif choice == 6:
        print("Exit")
        break
    else:
        print("Invalid choice!")
        