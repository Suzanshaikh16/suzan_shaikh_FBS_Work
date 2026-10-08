def decorator(a):
    def wrapper(*args):
        print('Time Started')
        print('Logger Added')
        a(*args)
        print('Time stopped')
        print('Logger removed')
    return wrapper
@decorator
def login():
    print('\nLog in is Done\n')
login()
#res=decorator(login)
#res()
@decorator
def add(a,b):
    print(a+b)
add(12,3)