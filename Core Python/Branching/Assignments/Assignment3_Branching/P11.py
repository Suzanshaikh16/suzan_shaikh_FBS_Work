a =int(input('Enter age of person1: '))
b =int(input('Enter age of person2: '))
c =int(input('Enter age of person3: '))
d =int(input('Enter age of person4: '))
e =int(input('Enter age of person5: '))
ticket =int(input('Ticket amt per person: '))

if(a<12):
    t1 = ticket-(ticket*30/100)
elif(a>59):
    t1 = ticket-(ticket*50/100)
else:
    t1 = ticket
if(b<12):
    t2 = ticket-(ticket*30/100)
elif(b>59):
    t2 = ticket-(ticket*50/100)
else:
    t2 = ticket
if(c<12):
    t3 = ticket-(ticket*30/100)
elif(c>59):
    t3 = ticket-(ticket*50/100)
else:
    t3 = ticket
if(d<12):
    t4 = ticket-(ticket*30/100)
elif(d>59):
    t4 = ticket-(ticket*50/100)
else:
    t4 = ticket
if(e<12):
    t5 = ticket-(ticket*30/100)
elif(e>59):
    t5 = ticket-(ticket*50/100)
else:
    t5 = ticket

total = t1+t2+t3+t4+t5
print('Total amt of ticket to travel all of them: ',total)
 
