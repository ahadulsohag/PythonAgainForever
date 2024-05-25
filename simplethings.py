#tuple
atuple = ("dfd", 3, "df", 834, 4)
print(atuple)
tuple2 = tuple()
print(tuple2)
print(atuple[2])
print(atuple[4:])
print(atuple[::-1])
print(type(atuple))
a = ("df")
print(type(a))
a = ("df",)
print(type(a))
if "dfd" in atuple:
    print("Yes")
else:
    print("No")
print(len(atuple))
print(atuple.count("df"))
print(atuple.index(4))
alist = ["df", "khk", 4]
print(alist.index(4))
alist = tuple(atuple)
print(alist)
print(type(alist))
atuple = list(alist)
print(atuple)
print(type(atuple))
xy = (1, 2, 3, 6)
q, w, e, r = xy
print(q)
print(w)
print(e)
print(r)
#unpacking tuple
i1, *i2, i3 = xy
print(i1)
print(i3)
print(i2)
i5 = list(xy)
print(i5)
import sys
print(sys.getsizeof(i5), "bytes")
print(sys.getsizeof(xy), "bytes")
import timeit
print(timeit.timeit(stmt= "(1, 2, 3, 4, 5)", number = 1000000))
print(timeit.timeit(stmt= "[1, 2, 3, 4, 5]", number = 1000000))