gender=str(input('enter gender male/female: '))
age=int(input('enter age: '))
if(gender=='female'):
    if(age>=18):
        print('girl is eligible for marriage')
    else:
        print('pehle padhai kar le')
else:
    if(gender=='male'):
        if(age>=21):
            print('boy is eligible')
    else:
        print('boy is not eligible')
