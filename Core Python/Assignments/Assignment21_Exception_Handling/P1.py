try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    op = input("Enter operator (+, -, *, /): ")

    if op == "+":
        print("Result:", num1 + num2)

    elif op == "-":
        print("Result:", num1 - num2)

    elif op == "*":
        print("Result:", num1 * num2)

    elif op == "/":
        print("Result:", num1 / num2)

    else:
        raise ValueError("Invalid operator")

except ValueError as e:
    print("Error:", e)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")