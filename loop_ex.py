count = 0
value = "y"
print(type(value))
while value:
  count+=1
  print(count)
  if(count==5):
    break
  else:
    value=True
    continue

print(type(value))