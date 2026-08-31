#1. ()
# tu = (10, 20, 30, 40)
tu = (10,)

#2. heterogeneous
tu = (10, 'abc' ,3.14)

#3. Ordered

#4. Immutable
tu[0] = 7

#5. Duplication allowed
#6. Faster than list
print(type(tu))
print(tu)

import sys
print(sys.getsizeof(tu))

