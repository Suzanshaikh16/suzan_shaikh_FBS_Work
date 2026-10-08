#1.step first
import demo
demo.add(12,4)
print(demo.pname)
#2.from modulename import member
from demo import add
add(12,5)

#3.from modulename import members
from demo import add,pname
add(12,5)
print(pname)

#4.from modulename import all(*)
from demo import *
add(12,4)
sub(12,3)
print(pname)

#5.Alicename()
import demo as d
d.add(12,8)
d.sub(12,3)
print(d.pname)