
import pickle

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print("ID:", self.eid)
        print("Name:", self.ename)
        print("Basic Salary:", self.basic)


def read_records():
    try:
        f = open("emp.dat", "rb")
        records = pickle.load(f)
        f.close()

        if isinstance(records, list):
            return records
        else:
            return [records]

    except FileNotFoundError:
        return []


def save_records(records):
    f = open("emp.dat", "wb")
    pickle.dump(records, f)
    f.close()


while True:
    print("\n1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    ch = int(input("Enter your choice: "))
    records = read_records()

    if ch == 1:
        eid = int(input("Enter ID: "))
        ename = input("Enter Name: ")
        basic = float(input("Enter Basic Salary: "))

        records.append(Emp(eid, ename, basic))
        save_records(records)
        print("Record added successfully")

    elif ch == 2:
        eid = int(input("Enter ID to search: "))
        found = False

        for e in records:
            if e.eid == eid:
                e.display()
                found = True
                break

        if not found:
            print("Record not found")

    elif ch == 3:
        eid = int(input("Enter ID to delete: "))
        found = False

        for e in records:
            if e.eid == eid:
                records.remove(e)
                found = True
                break

        if found:
            save_records(records)
            print("Record deleted successfully")
        else:
            print("Record not found")

    elif ch == 4:
        eid = int(input("Enter ID to edit: "))
        found = False

        for e in records:
            if e.eid == eid:
                e.ename = input("Enter new Name: ")
                e.basic = float(input("Enter new Basic Salary: "))
                found = True
                break

        if found:
            save_records(records)
            print("Record updated successfully")
        else:
            print("Record not found")

    elif ch == 5:
        if len(records) == 0:
            print("No records available")
        else:
            for e in records:
                e.display()
                print("----------------")

    elif ch == 6:
        print("Program ended")
        break

    else:
        print("Invalid choice")
