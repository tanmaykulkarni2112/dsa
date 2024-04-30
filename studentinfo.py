import os

# Function to add student information
def add_student_info():
    roll_number = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    division = input("Enter Division: ")
    address = input("Enter Address: ")
    with open("student_info.txt", "a") as file:
        file.write(f"{roll_number},{name},{division},{address}\n")
    print("Student information added successfully.")

# Function to delete student information
def delete_student_info():
    roll_number = input("Enter Roll Number of the student to delete: ")
    temp_file = open("temp.txt", "w")
    with open("student_info.txt", "r") as file:
        for line in file:
            if roll_number not in line.split(",")[0]:
                temp_file.write(line)
    temp_file.close()
    os.remove("student_info.txt")
    os.rename("temp.txt", "student_info.txt")
    print("Student information deleted successfully.")

# Function to display information of a particular student
def display_student_info():
    roll_number = input("Enter Roll Number of the student to display: ")
    with open("student_info.txt", "r") as file:
        found = False
        for line in file:
            if roll_number in line.split(",")[0]:
                found = True
                print("Student Information:")
                print("Roll Number:", line.split(",")[0])
                print("Name:", line.split(",")[1])
                print("Division:", line.split(",")[2])
                print("Address:", line.split(",")[3])
                break
        if not found:
            print("Student not found.")

# Main program
while True:
    print("\nStudent Information Management System")
    print("1. Add Student Information")
    print("2. Delete Student Information")
    print("3. Display Student Information")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student_info()
    elif choice == '2':
        delete_student_info()
    elif choice == '3':
        display_student_info()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
