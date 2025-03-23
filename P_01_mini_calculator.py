def Calculation():
    while True:
        choice = int(input("New calculation? Yes[1] or No[0]: "))
        
        if choice == 1:
            print("\nAddition[1] \nSubtraction[2] \nMultiplication[3] \nDivision[4]\n")
            n = int(input("Choose: "))

            # Addition
            def cal_sum():
                num1 = int(input("Enter 1'st number: "))
                num2 = int(input("Enter 2'nd number: "))
                print("Result: ", num1 + num2)

            # Subtraction
            def cal_Sub():
                num1 = int(input("Enter 1'st number: "))
                num2 = int(input("Enter 2'nd number: "))
                print("Result: ", num1 - num2)

            # Multiplication
            def cal_mul():
                num1 = int(input("Enter 1'st number: "))
                num2 = int(input("Enter 2'nd number: ")) 
                print("Result: ", num1 * num2)

            # Division
            def cal_div():
                num1 = int(input("Enter 1'st number: "))
                num2 = int(input("Enter 2'nd number: ")) 
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print("Result: ", num1 / num2)

            # Choose operation and execute
            if n == 1:
                cal_sum()
            elif n == 2:
                cal_Sub()
            elif n == 3:
                cal_mul()    
            elif n == 4:
                cal_div()
            else:
                print("Invalid choice. Please choose a valid operation.")
        
        elif choice == 0:
            print("Thank You For Using.")
            break
        else:
            print("Invalid input. Please enter 1 for Yes or 0 for No.")

# Start the calculator
Calculation()
