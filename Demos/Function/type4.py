#with passing parameters
#with returning value
def addition(num1, num2):
    

    add = num1+num2
    return add

num1 = int(input('enter num1: '))
num2 = int(input('enter num2: '))

res = addition(num1, num2)
print('Addition: ',res)
