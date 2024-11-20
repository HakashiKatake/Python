#Student Management Project
#Create a menu based Python application for maintaining student information (rollno, name,
#marks). It contains basic functions which include:
#i. Add student information
#ii. display student information,
#iii. search student using rollno
#iv. remove the student.
#v. display total number of students records


class Student:
    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks

    def display(self):
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Marks:", self.marks)

    def search(self, rollno):
        if self.rollno == rollno:
            self.display()
    
    def remove(self, rollno):
        if self.rollno == rollno:
            self.rollno = None
            self.name = None
            self.marks = None
            print(f"Student with Roll No: {rollno} has been removed.")
            return True
        print(f"Student with Roll No: {rollno} not found.")
        return False
    
    # New method to add student information with print statement
    def add_student(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks
        print(f"Student added: Roll No: {self.rollno}, Name: {self.name}, Marks: {self.marks}")

    # New method to display total number of students records with print statement
    @staticmethod
    def total_students(students):
        total = len(students)
        print(f"Total number of students: {total}")
        return total
    

print("Welcome to the Student Management System")

students = []

while True:
    print("1. Add Student")
    print("2. Display Student")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Total Students")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        rollno = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        student = Student(rollno, name, marks)
        students.append(student)
        student.add_student(rollno, name, marks)
    elif choice == 2:
        for student in students:
            student.display()
    elif choice == 3:
        rollno = int(input("Enter Roll No to search: "))
        for student in students:
            student.search(rollno)
        else:
            print("Student not found.")
    elif choice == 4:
        rollno = int(input("Enter Roll No to remove: "))
        for student in students:
            if student.remove(rollno):
                break
    elif choice == 5:
        Student.total_students(students)
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

