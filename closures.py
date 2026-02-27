def me(person):
  coins = 3
  def play_game():
    nonlocal coins
    coins-=1
    if coins>1:
      print("\n"+ person +" has "+str(coins)+" left.")
    elif coins == 1:
      print("\n" + person + " has "+ str(coins)+ " left.")
    else:
      print("\n"+ person + " is out of coin.")
  return play_game

tommy = me("A")
tommy = me("AB")
jenny = me("jenny")

tommy()
jenny()
tommy()
