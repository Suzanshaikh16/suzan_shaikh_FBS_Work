li = [10, 20, 30, 40, 50, 60]
def binarysearch(li, searchEle):
    beg = 0
    end = len(li)-1
    while(beg<=end):
        #print('beg:', beg)
        #print('end:', end)
        mid = (beg+end)//2
        #print('mid:', mid)
        #print('searchEle:',searchEle)
        #print('mid ele:',li[mid])
        if(searchEle == li[mid]):
            #print('match condition')
            return mid
        elif(searchEle < li[mid]):
            #print('less than')
            end = mid - 1
        elif(searchEle > li[mid]):
            #print('greater than')
            beg = mid + 1
    else:
        return -1
    
ele =int(input('Enter search element: '))
res = binarysearch(li, ele)
#print result
if(res!=-1):
    print(f'{ele} is present at index {res}')
else:
    print(f'{ele} is not present in a list')
