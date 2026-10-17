
r=20
l=50
b=40
rounds=5
rate=35

circle=2*3.14*r
rectangle=2*(l+b)

total_wire = (circle+rectangle)*rounds
cost = total_wire*rate

print("Total wire required:", total_wire,"metres")
print("Total cost of fencing: Rs.",cost)
