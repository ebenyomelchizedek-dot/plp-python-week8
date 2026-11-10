
# Welcome message
print("================================")
print(" Welcome to My Python Toolkit!")
print("================================")

# Create an empty list to store tasks
tasks = []

# Keep showing the menu until the user chooses to quit
while True:
    print("\nPlease choose a tool:")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Even or Odd Checker")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    # TOOL 1: Simple Calculator
    # Performs addition, subtraction, multiplication and division
    if choice == "1":
        print("\n--- Simple Calculator ---")

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            print("\nChoose an operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")

            operation = input("Enter operation (1-4): ")

            if operation == "1":
                result = num1 + num2
                print(f"The answer is: {result}")

            elif operation == "2":
                result = num1 - num2
                print(f"The answer is: {result}")

            elif operation == "3":
                result = num1 * num2
                print(f"The answer is: {result}")

            elif operation == "4":
                if num2 != 0:
                    result = num1 / num2
                    print(f"The answer is: {result}")
                else:
                    print("Sorry, you cannot divide by zero.")

            else:
                print("Invalid operation. Please choose 1-4.")

        except ValueError:
            print("Please enter valid numbers.")

    # TOOL 2: To-Do List
    # Allows the user to add and view tasks
    elif choice == "2":
        print("\n--- To-Do List ---")

        while True:
            print("\n1. Add a task")
            print("2. View tasks")
            print("3. Return to main menu")

            task_choice = input("Choose an option (1-3): ")

            if task_choice == "1":
                task = input("Enter your task: ")

                if task.strip():
                    tasks.append(task)
                    print(f"Task '{task}' added successfully!")
                else:
                    print("Task cannot be empty.")

            elif task_choice == "2":
                if len(tasks) == 0:
                    print("Your to-do list is empty.")
                else:
                    print("\nYour tasks:")
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

            elif task_choice == "3":
                print("Returning to the main menu...")
                break

            else:
                print("Invalid choice. Please select 1, 2 or 3.")

    # TOOL 3: Even or Odd Checker
    # Checks whether a number is even or odd
    elif choice == "3":
        print("\n--- Even or Odd Checker ---")

        try:
            number = int(input("Enter a whole number: "))

            if number % 2 == 0:
                print(f"{number} is an even number.")
            else:
                print(f"{number} is an odd number.")

        except ValueError:
            print("Please enter a valid whole number.")

    # QUIT THE PROGRAM
    elif choice == "4":
        print("\nThank you for using My Python Toolkit!")
        print("Goodbye and have a great day!")
        break

    # HANDLE INVALID MENU CHOICES
    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please try again.")
