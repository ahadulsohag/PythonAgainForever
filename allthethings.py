#String = immutable, ordered, text representation
astring = "Hello World!"
print(type(astring))
a = """Hello 
World
!"""
print(a)
a = """Hello \
World \
!"""
print(a)
print(a[0])
print(a[1:7])
print(a[::2])
print(a[::-1])
print(a[7:])
G = "Hello"
N = "Sohag"
print(G + " " + N)
d = G + " " + N
print(d)
x = 1
for i in G, N:
    print(x)
    x+=1
G = "    Soh            ag   "
G = G.strip()
print(G)
print(2334)
