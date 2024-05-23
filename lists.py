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