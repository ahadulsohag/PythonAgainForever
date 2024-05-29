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