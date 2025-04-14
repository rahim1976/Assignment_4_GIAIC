import random

def play():
  user = input("Whats Your Choice? , 'R' for Rock, 'P' for Paper, 'S' for scissors\n")
  computer = random.choice(['r','p','s'])

  if  user == computer:
    return 'Tie'

  # r > s , s > p , p > r
  if is_win(user, computer):
    return 'You Won!'

  # if is_win(computer, user):
  return 'You Lost!'

def is_win(player, opponent):
  #return true if player wins
  # r > s , s > p , p > r
  if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'):
    return True

print(play())