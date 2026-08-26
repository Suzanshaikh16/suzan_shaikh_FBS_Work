def emp(id,name,sal=0, dept= 'Backoffice'):
    print('ID:', id)
    print('Name:', name)
    print('SAL:',sal)
    print('DEPARTMENT:',dept)

emp(name = 'ABC',sal = 50000,dept ='IT',eid = 101)
print('#############')
emp(101,'XYZ',dept = 'IT', sal = 10000) 