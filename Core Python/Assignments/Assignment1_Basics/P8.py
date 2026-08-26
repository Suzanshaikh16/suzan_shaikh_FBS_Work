days = int(input('enter days: '))

years = days // 365
dayys = days % 365

weeks = dayys // 7

rdays = dayys % 7

print(years)
print(weeks)
print(rdays)

print(f'{years},{weeks},{rdays}')