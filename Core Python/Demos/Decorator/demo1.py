def demo():
    print('I am in demo')
x=demo
#demo()
x()
def demo(a):
    a()
def fun():
    print('I am in tested function')
demo(fun)

#return one function from other function
def outerfun():
    print('I am in inner outer')
    def innerfun():
        print('I am in inner function')
    return innerfun
    #return 10
result=outerfun()
result()