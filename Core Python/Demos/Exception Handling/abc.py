from myexception import MyException
try:
    age=int(input("Enter the Age="))
    if age<=0:
        #m=MyException(age)
        raise MyException(age)
except MyException as m:
    print(m)
except Exception as e:
    print(e)
    