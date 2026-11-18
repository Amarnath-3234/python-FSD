
class student:
    def __init__(self,usn, name, age, marks):
        self.usn = usn
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("USN:", self.usn)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("===================================")

class student_management:
    def __init__(self):
        self.students = []

    def add_student(self):
        usn = input("Enter USN: ")

        for existing_student in self.students:
            if existing_student.usn == usn:
                print("user already exists!")
                return
        name = input("Enter student name: ")
        while True:
            try:
                age = int(input("Enter student age: "))
                break
            except ValueError:
                print("Please enter a valid whole number for age.")

        while True:
            try:
                marks = float(input("Enter marks: "))
                break
            except ValueError:
                print("Please enter a valid number for marks.")

        new_student = student(usn, name, age, marks)

        self.students.append(new_student)

        print("Student added successfully!")

    def view_students(self):

        if len(self.students) == 0:
            print("No students found!")
            return

            for student in self.students:
                student.display()

    def search_student(self):
        usn = input("Enter USN to search: ")

        for student in self.students:
            if student.usn == usn:
                print("Student found!")
                student.display()
                return

        print("Student not found!")
        
    def delete_student(self):
        usn = input("Enter USN to delete: ")

        for student in self.students:
            if student.usn == usn:
                self.students.remove(student)
                print("Student deleted!")
                return
            
        print("Student not found!")

app = student_management()

while True:
    print("\n=========Student Management System=========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        app.add_student()
    elif choice == "2":
        app.view_students()
    elif choice == "3":
        app.search_student()
    elif choice == "4":
        app.delete_student()
    elif choice == "5":
        print("thank you for using the student management system!")
        break

    else:
        print("Invalid choice! Please try again:")        