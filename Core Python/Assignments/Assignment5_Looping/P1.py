correct_u ="suzan"
correct_p="1234"
for i in range(0,3):
    u =str(input('Enter User ID: '))
    p =int(input('Enter Password: '))
    if(u==correct_u and p==correct_p):
        print('Login successful')
        break
    else:
        print('Incorrect User ID and Password')
else:
    print('You have used all 3 attempts.')
    print('Program terminated.')

