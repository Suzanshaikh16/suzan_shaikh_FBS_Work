emp_details = {}
def addEmp():
    id = int(input("Enter ID: "))
    nm = input("Enter NAME: ")
    dept = input("Enter DEPARTMENT: ")
    sal = float(input("Enter SALARY: "))
    if id not in emp_details:
        emp_details[id] = [id, nm, dept, sal]
        return "Employee added successfully."
    else:
        return "Employee ID already available."
def updEmp():
    id = int(input("Enter ID: "))
    er = emp_details.get(id)
    if er:
        nm = input(f"Enter new NAME ({er[1]}): ") or er[1]
        dept = input(f"Enter new DEPT ({er[2]}): ") or er[2]
        sal = input(f"Enter new SALARY ({er[3]}): ") or er[3]
        sal = float(sal)
        emp_details[id] = [id, nm, dept, sal]
        return "Employee updated successfully."
    else:
        return "ID not found."
def delEmp():
    id = int(input("Enter ID: "))
    if id in emp_details:
        del emp_details[id]
        return "Employee deleted successfully."
    else:
        return "ID not found."
def searchEmp():
    id = int(input("Enter ID: "))
    er = emp_details.get(id)
    if er:
        return f"ID: {er[0]}, Name: {er[1]}, Department: {er[2]}, Salary: {er[3]}"
    else:
        return "ID not found."
def showAllEmp():
    if emp_details:
        for er in emp_details.values():
            print(
                f"ID: {er[0]}, Name: {er[1]}, "
                f"Department: {er[2]}, Salary: {er[3]}"
            )
    else:
        print("No employees available.")
def empManage():
    while True:
        print("\n#### EMPLOYEE MANAGEMENT ####")
        print("Please select option from below:")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Search Employee")
        print("5. Show All Employees")
        print("6. Logout")
        ch = input("Enter choice: ")
        if ch == '1':
            res = addEmp()
            print(res)
        elif ch == '2':
            res = updEmp()
            print(res)
        elif ch == '3':
            res = delEmp()
            print(res)
        elif ch == '4':
            res = searchEmp()
            print(res)
        elif ch == '5':
            showAllEmp()
        elif ch == '6':
            print("Logged out...")
            break
        else:
            print("Invalid choice...")
def login():
    print("\n#### LOGIN PAGE ####")
    uid = 'admin'
    passw = '1234'
    username = input("Enter USERNAME: ")
    password = input("Enter PASSWORD: ")
    if uid == username and passw == password:
        empManage()
    else:
        print("Invalid credentials...")
def main():
    ch = '0'
    while ch != '2':
        print('''
Please select option from below:
1. Login page
2. Exit
''')
        ch = input("Enter choice: ")
        if ch == '1':
            login()
        elif ch == '2':
            print("Thank you for choosing us!")
        else:
            print("Invalid choice...")
main()