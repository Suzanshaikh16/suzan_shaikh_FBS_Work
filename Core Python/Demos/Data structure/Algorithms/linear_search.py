li = [45, 67, 23, 89, 56, 13, 10, 90]
def linearsearch(li, searchelemt):
    for ind in range(0,len(li)):
        if(searchelemt==li[ind]):
            return ind
    else:
        return -1
ele =int(input('Enter search element: '))
res = linearsearch(li, ele)
#print result
if(res!=-1):
    print(f'{ele} is present at index {res}')
else:
    print(f'{ele} is not present in a list')
