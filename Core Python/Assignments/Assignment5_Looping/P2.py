n =int(input('Enter number of students: '))
average = 0
for i in range(1,n+1):
    s1 =int(input('Enter marks of s1: '))
    s2 =int(input('Enter marks of s2: '))
    s3 =int(input('Enter marks of s3: '))
    s4 =int(input('Enter marks of s4: '))
    s5 =int(input('Enter marks of s5: '))
    percent =(s1+s2+s3+s4+s5)/500*100
    print('Percentage: ',percent)
    average = average + percent

average_p = average / n
print('Average Percentage: ',average_p)

