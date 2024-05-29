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
print(G.upper())
print(G.lower())
print(G.startswith("S"))
print(G.endswith("df"))
print(G.find("a"))
print(G.count("g"))
print(G.replace("ag", "ga"))
w = "Hey, Whats up!"
d = w.split(" ")
print(d)
w = "Hey,Whats,up!"
d = w.split(" ")
print(d)
w = "Hey Whats up!"
d = w.split(" ")
print(d)
s = " ".join(d)
print(s)
wd = ["a"] * 3
print(wd)
ds = "".join(wd)
print(ds)
ds = " ".join(wd)
print(ds)