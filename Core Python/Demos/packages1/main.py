# 1.Direct import
import mypack.abc
import mypack.xyz
mypack.abc.greet()
a=mypack.xyz.iname
print(a)
mypack.xyz.greet1()
#2From pakagename.modulename import member
from mypack.abc import greet
greet()
#3From pakagename. modulename import members
from mypack.abc import greet
from mypack.xyz import greet1,iname
greet()
print(iname)
greet1()
#4from packagename.modulename import all(*) members
from mypack.abc import greet
from mypack.xyz import *
greet()
print(iname)
greet1()
