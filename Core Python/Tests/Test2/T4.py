
l=float(input("Enter length of wall: "))
h=float(input("Enter height of wall: "))
r=float(input("Enter painting cost per sq.m: "))

area = 4*l*h
total = area * r

print("Total area of four walls:", area,"sq.m")
print("Total painting cost: Rs.", total)
