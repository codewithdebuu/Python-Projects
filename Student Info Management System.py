# Project Name: Student Info Management System
# Description: A simple program to add and search student records saved in a file.

class Student(object):
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        print("\nInformation updated!")

    def show_info(self):
        print(f"Student name: {self.name} & roll: {self.roll}.\n")


def stu_data():
    while True:
        print("\nWhat do you want?")
        print("1 = Enter Student Information    |   2 = Search  |   0 = Exit \n")

        while True:
            try:
                decision = int(input("Enter number: "))
                if decision in [0, 1, 2]:
                    break
                else:
                    print("Please enter 0, 1, or 2\n")
            except ValueError:
                print("Please enter a valid number: 0, 1, or 2\n")
        
        if decision == 0:
            print("Exiting...")
            break
        
        elif decision == 1:
            new_name = input("Student Name: ").strip()  
            while True:
                try:
                    new_roll = int(input("Student Roll: "))
                    break
                except ValueError:
                    print("Please enter a valid roll number.\n")
            
            # Append Student Data to the file
            with open("Stu_info_project.txt", "a") as f:
                f.write(f"Student Name: {new_name} & Roll: {new_roll}.\n")
            
            stu_info = Student(new_name, new_roll)
            stu_info.show_info()

        elif decision == 2:
            try:
                with open("Stu_info_project.txt", "r") as f:
                    lines = f.readlines()
            except FileNotFoundError:
                print("No Student Database Found! Please add some students first.")
                continue  

            word = input("Enter Name or Roll to search: ").strip()
            found = False
            print()
            for line in lines:
                if word.lower() in line.lower():
                    print("Found:", line.strip())
                    found = True

            if not found:
                print(f"The {word} was Not Found in the Database.\n")

# Start the program
stu_data()
