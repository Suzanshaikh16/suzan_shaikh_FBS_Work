try:
    n1=int(input('enter no.1: '))
    n2=int(input('enter no.2: '))
    div =(n1//n2)
    print(div)
except ZeroDivisionError as a:
    print(f"I am in zerDiv",a)
except ValueError as v:
    print(f"Value err={v}")
except Exception as e:
    print(e)
else:
    print("I am in else Block")
finally:
    print("I am in finally block")