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