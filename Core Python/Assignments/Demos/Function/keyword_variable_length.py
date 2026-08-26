
def emp(**data):
    for key, val in data.items():
        print(key,':',val)

emp(id = 101, age = 35,add ='Pune', sal=50000, dept= 'Admin')