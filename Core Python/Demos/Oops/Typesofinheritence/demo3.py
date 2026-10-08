class emp():
    def calsal(self):
        print('Empcalsal')
class Hr(emp):
    def calsal(self):
        print('Hr calsal')
class admin(emp):
    def calsal(self):
        print('admin calsal')
h = Hr()
a = admin()

h.calsal()
a.calsal()