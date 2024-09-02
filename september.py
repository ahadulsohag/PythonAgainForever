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
blist = [2, "School", "School", "college"]
print(type(blist))
print(blist)
btuple = tuple(blist)
print(type(btuple))
print(btuple)
for i in btuple:
    print(i)