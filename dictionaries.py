user = {"Name": "Sohag", "Age": 23, "Institute": "SMUCT", "dfds": "df", "kkk": "r343"}
print(user)
user ["Email"] = "aha@gmail.com"
print(user)
user2 = dict(dfd = "dfd", kjl = "kjk" )
print(user2)
del user[("Name")]
print(user)
user.popitem()
print(user)
user.pop("Age")
print(user)
print(user)
if "Institute" in user:
    print(user["Institute"])
try:
    print(user["Institute"])
except:
    print("Error")
try:
    print(user["fd"])
except:
    print("Error")
for i in user:
    print(i)
print(user.keys())
print(user.values())
for i, j in user.items():
    print(i, j)
k = {"fd":"dfd", "32423": "jkj", 3:"kj"}
j = k
print(type(j))
