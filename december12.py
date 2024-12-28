alist = [1, 2, 3, 4, 5]
blist = alist[:]
blist.append(6)
print(blist)
print(alist)
B = [1, 2, 3, 4, 5]
C = [i*i for i in B]
print(C)
atuple = (1,)
print(type(atuple))
c = (1, 2, 3, 4, 5)
d = c[::-1]
print(d)
d = [i*i for i in d] 
print(d)
i = (1, 2, 3, 4, 5)
i1, i2, i3, i4, i5 = i
print(type(i2))