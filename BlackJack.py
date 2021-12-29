import random

def create_deck():
  faces = ['A', '2', '3', '4','5','6','7','8', '9', 'T', 'J', 'Q', 'K']
  suits = ['H', 'C', 'S', 'D']
  deck = []
  for i in range(0,4):
    for k in range(0,13):
      deck.append(faces[k]+suits[i])
  return deck

def draw_card(deck):
  card = random.choice(deck)
  deck.remove(card)
  return card

def draw_hands(deck):
  player_hand = [draw_card(deck), draw_card(deck)]
  dealer_hand = [draw_card(deck), draw_card(deck)]
  return player_hand,dealer_hand


def print_hands(player_hand, dealer_hand, GAMEOVER):
  print("This is the player's hand: ")
  print(player_hand)
  player_total = get_hand_total(player_hand)
  print("This is the total of your cards:")
  print(player_total)
  if not GAMEOVER:
    print("\nThis is the dealers hand: ")
    print([dealer_hand[0], "??"])
  else:
    print("\nThis is the dealers hand: ")
    print(dealer_hand)


def hitOrStand(player_hand, dealer_hand, deck):
  hitOrStand = input("\nWould you like to hit or stand (s) to stand or (h) to hit?: ").lower()
  if hitOrStand == "h":
    new_card = draw_card(deck)
    player_hand.append(new_card)
    print("\nYour new card is "+new_card)
    return check_bust(player_hand)
  elif hitOrStand == "s":
    dealer_total = get_hand_total(dealer_hand)
    while dealer_total < 17:
      new_card = draw_card(deck)
      dealer_hand.append(new_card)
      dealer_total = get_hand_total(dealer_hand)
    return True

def get_hand_total(hand):
  
  total = 0 
  num = 0
  for i in range(len(hand)):
    if hand[i][0] == "A":
      num += 1
      total += 1
    elif hand[i][0] in "TQJK":
      total += 10
    else:
      total += int(hand[i][0])
  
  if total < 12 and num > 0:
    total += 10

  return total

def check_bust(hand):

  if get_hand_total(hand) > 21:
    print("\nYou have gone bust")
    return True

  return False

def who_won(player_hand, dealer_hand):

  if check_bust(player_hand):
    return "DEALER"
  if check_bust(dealer_hand):
    return "PLAYER"
  
  player_total = get_hand_total(player_hand)
  dealer_total = get_hand_total(dealer_hand)

  if player_total > dealer_total:
    return "PLAYER"
  elif player_total < dealer_total:
    return "DEALER"
  else:
    return "TIE"
  return(player_total,dealer_total)


def main():
  play_again = True
  while play_again:
    GAMEOVER = False
    deck = create_deck()
    player_hand, dealer_hand = draw_hands(deck)
    print_hands(player_hand,  dealer_hand, GAMEOVER)

    while not GAMEOVER:
      GAMEOVER = hitOrStand(player_hand, dealer_hand, deck)
      print_hands(player_hand,  dealer_hand, GAMEOVER)
      
    winner = who_won(player_hand,  dealer_hand)


    print("The winner is: {}!!!".format(winner))

    play_again = input("\nWould you like to play again? (Y/N): ").lower() == 'y'

    #Print the rules, welcomes etc
    #Draw player hands and dealer hands
    #Show the cards
    #Ask the user to hit or stand
    #If they hit, draw a new card, check if they bust
    #If they stand, dealer to draw until they have >= 17
    #Decide who wins

  return


if __name__ == "__main__":
  main()