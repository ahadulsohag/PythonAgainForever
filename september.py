newlist = [2, 3, 7, 9, 9, 0]
print(newlist)
extra = [i*i for i in newlist]
print(extra)
atuple = ("cat", "dog")
print(type(atuple))
atuple = "man", "woman"
print(type(atuple))
atuple = "citizen"
print(type(atuple))
atuple = "citizen", 
print(type(atuple))
blist = [2, "Myself", "School", "School", "college"]
print(type(blist))
print(blist)
btuple = tuple(blist)
print(type(btuple))
print(btuple)
for i in btuple:
    print(i)
print(len(btuple))
print(btuple.count("School"))
print(btuple.index("School"))
clist = list(btuple)
print(clist)
print(type(clist))
ctuple = (tuple(clist))
print(ctuple)
print(type(ctuple))
import sys
import timeit
numtuple = 1, 3, 4, 8, 9, 68, 342342345234, 8979789,
numlist = [1, 3, 4, 8, 9]
print(sys.getsizeof(numlist), "bytes")
print(sys.getsizeof(numtuple), "bytes")
print(timeit.timeit(stmt= "[1, 2, 8, 9]", number= 10000))
print(timeit.timeit(stmt= "1, 2, 8, 9", number= 10000))
print(type(numtuple))
print(numtuple[::-1])
i1, i2, i4, *i5,  = numtuple
print(i1)
print(i2)
print(i4)
print(i5)