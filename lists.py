alist = ["apple", "banana", "guava"]
print(alist)
alist1 = list()
print(alist1)
alist = [1, True, "banana"]
print(alist)
print(alist[-3])
for i in alist:
    print(i)
if "guava" in alist:
    print("Yes")
else:
    print("No")
print(len(alist))
alist.append("Strawberry")
print(alist)
alist.insert(0, "Pineapple")
print(alist)
item = alist.pop()
print(item)
print(alist)
alist.remove("banana")
print(alist)
print(len(alist))
alist.reverse()
print(alist)
alist= [1, 3, 0, 4, 9]
slist = sorted(alist)
print(slist)
alist.sort()
print(alist)
alist.clear()
alist = [4] * 3
print(alist)
alist1  = [2, 43, 4] + alist
print(alist1)