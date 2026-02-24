def pf(a):
  coin = 3
  print(coin)
  def game():
    nonlocal coin
    print(type(coin))
    print(coin)
  game()


pf(2)