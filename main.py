students = []

choice = 0
def print_student(student):
    print("Name : ", student["name"])
    print("Age: ", student["age"])
    print("Course: ", student["course"])

def find_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None

def delete_student(student):
    if student:
        students.remove(student)
        print("Student deleted Successfully.")
    return None

def get_valid_age():
    while True:
        try:
            age = int(input("Enter Student Age: "))

            if 1 <= age <= 120:
                return age
            else:
                print("Age must be between 1 and 120.")

        except ValueError:
            print("Please enter a valid number.")

def add_student():
    print("You selected Add Student")
    name = input("Enter Student Name: ")           
    age = get_valid_age()
    course = input("Enter Student Course: ")
    student_data = {
                "name" : name,
                "age" : age,
                "course" : course
            }
    students.append(student_data)
    print("Student added successfully!")

def view_students():
    print("You selected View Student")
    i = 1
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print(f"""-------------------- \n    Student {i}\n--------------------""")
            print_student(student)
            i+= 1

def search_student_menu():
    print("You selected Search Student")
    search_student= input("Enter the student name: ")
    student = find_student(search_student)
    if student:
        print_student(student)
    else:
        print("Student not found.")

def delete_student_menu():
    print("You selected Delete Student")
    delete_name = input("Enter the student name: ")
    student = find_student(delete_name)
    if student:
        delete_student(student)
    else:
        print("Student not found.")

def update_student_menu():
    print("You selected update student")
    update_student = input("Enter the Student name: ")
    student = find_student(update_student)
    if student:
        update_field = input("Which field do you want to update:").lower()
        if(update_field == "name"):
            name = input("Enter the name: ")
            student["name"] = name
            print("Student updated successfully!")
        elif(update_field == "age"):   
            student["age"] = get_valid_age()
            print("Student updated successfully!")
        elif(update_field == "course"):
            course = input("Enter the course: ")
            student["course"] = course
            print("Student updated successfully!")
        else:
            print("Please enter a valid input")
    else:
        print("Student not found.")

while (choice != 6):
    print("""
===== Student Record Management =====

1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Update Student
6. Exit
""")
    try:
        choice = int(input("Enter your Choice: "))
    except ValueError:
        print("Please Enter a Valid Number")
        continue
    if (choice < 1 or choice > 6):
        print("Please enter a Valid Number")

# Add Student
    elif (choice == 1):
        add_student()
# View Students 
    elif (choice == 2):
        view_students()
# Search Students
    elif (choice == 3):
        search_student_menu()
# Delete Students
    elif (choice == 4):
        delete_student_menu()
# Update Students
    elif(choice == 5):
        update_student_menu()
# Exit
    elif (choice == 6):
        print("Thank you for using Student Record Management System.")