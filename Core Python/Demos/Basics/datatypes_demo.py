#numeric 1.int
var=10
var=3.14
print(type(var))
#2.float
var=3.14
#3.complex
var=10+5j
print(type(var))

##Text
#str
var='first "bit" solutions'
var="firstbit's solutions"
var='''firstbitsolutions.ghj.jkl'''
var="""hjkl;kjhg;klo"""

print(type(var))

##sequential
#list
var=[10,8,7,4,3]
print(type(var))
#tuple
var=(10,9,8,7)
print(type(var))
#range
var=range(1,11)
print(type(var))

##Set type
#set
var={2,3,4}
print(type(var))
#frozenset
var=frozenset({2,4,6})
print(type(var))

##mapping
#dict
var={'id':101,'name':'suzan'}
print(type(var))

##Others
#boolean
var=True
print(type(var))
#none type
var=None
print(type(var))

