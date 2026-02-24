def afunc(num1):
  if(num1>=10):
    return num1
  res = num1+1
  print(res)
  return afunc(res)
  

afunc(1)