name = "sohag"
def pna(fn):
  print(fn)

pna(name)

def hi():
  color = "red"
  print(color)
  def hello():
    nonlocal color
    color = "yellow"
    print(color)
  hello()
  
hi()