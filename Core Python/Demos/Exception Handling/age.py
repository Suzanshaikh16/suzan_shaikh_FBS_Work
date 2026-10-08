try:
    a=int(input('Enter age: '))
    if a<=0:
        raise ZeroDivisionError("Enter valid a")
except Exception as e:
    print(e)