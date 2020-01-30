#5 & 6 & 7
win_dict = {

}
while True:
  number = 0
  whoWon = input("Who has won this match?\n> ").title()
  if whoWon == "End":
    break
  if winner in win_dict.keys():
    win_dict[winner] += 1
  else:
    win_dict[winner] = 1
  for key,value in win_dict.items():
    print('{} {}wins'.format(key,value))