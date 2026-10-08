class Emp:
    def __init__(self, id, name, sal):
        self.eid = id #public:Everywhere in code
        self._name = name #protected: Available in class
        self.__sal = sal #private: Only available inside class
e1 = Emp(101, 'ABC', 50000)

print(e1.eid)
print(e1._name)#Not worked in python
# print(e1.__sal) #raise error
print(e1._Emp__sal)