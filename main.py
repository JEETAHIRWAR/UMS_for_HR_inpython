# employees = []

employees = [
    ["Jeet", "Developer", 50000],
    ["Rahul", "Designer", 40000],
    ["Aman", "Manager", 65000],
    ["Priya", "HR", 35000],
    ["Rohit", "Tester", 30000],
    ["Sneha", "Data Analyst", 55000],
    ["Karan", "Backend Developer", 70000],
    ["Neha", "Frontend Developer", 48000],
    ["Arjun", "Cyber Security Analyst", 75000],
    ["Pooja", "UI/UX Designer", 42000]
]

while True:

    print('\n--- Employee Management System')
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Remove Employee")
    print("5. Update Employee Salary")
    print("6. Total Employees")
    print("7. Sort Employees")
    print("8. Reverse Employee List")
    print("9. Exit")

    choice = input("Enter Choice: ")
#1. Add Employee
    if choice == "1":
        name = input("Enter Employee Name: ")
        designation = input("Enter Designation: ")
        salary = int(input("Enter Salary: "))
        employee = [name, designation, salary]
        employees.append(employee)
        print("Employee Added Sucessfully")
#2. View Employees
    elif choice =="2":
        print("\nEmployee List:")

        for emp in employees:
            print("Name:", emp[0])
            print("Designation:", emp[1])
            print("Salary:", emp[2])
            print("-----------------")

    # SEARCH EMPLOYEE
    elif choice == "3":

        search_name = input("Enter Employee Name to Search: ")
        # found = False

        for emp in employees:
            if emp[0].lower() == search_name.lower():
                print("\nEmployees Found")
                print("Name: ", emp[0])
                print("Designation: ", emp[1])
                print("Salary: ", emp[2])

                found = True
                break
        if found == False:
            print("Employee Not Found")

    # REMOVE EMPLOYEE
    elif choice == "4":

        remove_name = input("Enter Employee Name to Remove:")
        found = False

        for emp in employees:
            if emp[0].lower() == remove_name.lower():
                employees.remove(emp)
                print("Employee Removed Sucessfully")
                found = True
                break
        if found == False:
            print("Employee Not Found")

    #5. Update Employee Salary
    elif choice == "5":
        update_name = input("Enter Employee Name")
        found = False

        for emp in employees:
            if emp[0] == update_name:
                new_salary = int(input("Enter New Salary: "))
                emp[2] = new_salary
                print("Salary Updated Sucessfully")

                found = True
                break
        if found == False:
            print("Employee Not Found")

    #6. Total Employees
    elif choice == "6":
            print("Total Employees:", len(employees))
        
    #7. Sort Employees
    elif choice == "7":
        employees.sort()
        print("Employees Sorted Sucessfully")
    
    #8. Reverse Employee List
    elif choice == "8":
        employees.reverse()
        print("Employees List Reversed")

#5. Program Exit
    elif choice == "9":
        print("Program Closed")
        break
    else:
        print("Invalid choice")