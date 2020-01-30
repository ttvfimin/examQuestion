#5 & 6 & 7
winners = []
winnersNum = []
while True:
  number = 0
  whoWon = input("Who has won this match?\n> ").title()
  if whoWon == "End":
    break
  elif whoWon == "Remove":
    whoRemove = input("Who do you want to remove?\n> ").title()
    try:
      winners.remove(whoRemove)
    except ValueError:
      print("That person hasn't won yet!")
  else:
    winners.append(whoWon)
  for winner in winners:
    print(winner)