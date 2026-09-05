area = float(input('Enter area of one wall: '))
i = float(input('Enter cost of interior wall: '))
e = float(input('Enter cost of exterior wall: '))

itotal = 8*area*i
etotal = 6*area*e

tcost = itotal+etotal

print('Interior painting cost =', itotal)
print('Exterior painting cost =', etotal)
print('Total painting cost =', tcost)