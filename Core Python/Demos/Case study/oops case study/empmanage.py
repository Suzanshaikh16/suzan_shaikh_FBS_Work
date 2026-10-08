from hr import Hr
from dev import Dev
class EmpManage:
    Empdetil={}
    def addEmp(self):
        eid=input("Enter  Emp Id ")
        if eid in EmpManage.Empdetil:
            print("Employee is Aalredy Exist...")
            return
        else:
            ename=input("Enter the EMp  Name= ")
            esal=float(input("Eneter Emp  sal "))
            print("1.Hr")
            print("2.Devloper ")
            ch=int(input("Enter the Choice= "))
            if ch==1:
                ecom=float(input("enter the com of Hr= "))
                emp=Hr(eid,ename,esal,ecom)
            elif ch==2:
                bonus=float(input("enter the Bonus of Dev= "))
                emp=Dev(eid,ename,esal,bonus)
            else:
                print("Inavaldi choice ")
                return
            EmpManage.Empdetil[eid]=emp
            print("Emp added sussefully....")
    def displyEmp(self):
        if len(EmpManage.Empdetil)==0:
            print("Emp is not Exist,..... ")
        else:
            for var in EmpManage.Empdetil.values():
                print(var)
    def searchEmp(self):
        print("I am in Search")
    def UpdateEmp(self):
        print("I am in Update")
    def deleteEmp(self):
        print("I am in Delete")