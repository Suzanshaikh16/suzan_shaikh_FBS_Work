userid =str(input('Enter userid: '))
passwd =int(input('Enter password: '))
if(userid=='suzan' and passwd==1234):
    print('Capcha:7744')
    capcha=int(input('Enter provided capcha: '))
    if(capcha==7744):
    
        print('login successful')
    else:
        print('login unsuccessful')
else:
    print('Invalid userid and password')