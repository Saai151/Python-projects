import random

"""
TODO:
  - Ascii Art (Optional)
  - Extension: type the letters on keyboard
"""
## Returns the hashed word
def hash_word(word):
  return "#"*len(word)

## Returns the user's guess and makes sure that the user isn't guessing the same letter again
def good_valid_guess(guesses):
  
  valid_input = False
  while not valid_input:
    user_guess = input("Please make your guess: ").lower()
    if user_guess in guesses:
      print("You guessed the same letter please guess a different one.")
    elif not user_guess.isalpha():
      print("That isn't a valid input please enter again")
    else:
      valid_input = True 

  return user_guess

## shows the user the words they have guessed 
def show_alphabet(alphabet):
 
  print("\nThe letters that you have guessed are:")
  print(" ".join(alphabet))

# def test_func(x):

#   return x+1, x+2

# x = test_func(1)
# print(x[0], x[1])

## checks to see if users guess is the chosen word
def parameters_word_chosen(word, guess):
  if word == guess:
    return True

## Decides whether or not user won
def win_conditions(lives):
  if lives > 0:
    print("\nCongratulations you got the word right!")
  elif lives <= 0:
    print ("You have run out of guesses please restart the game!")

word_list = ("cap disturbed rhyme known collect existence innocent blush reduce macho blue basketball insurance shaggy jump cheerful cloudy thumb chivalrous dreary release list prickly cushion lyrical vulgar outrageous careless direction erratic guttural solid welcome perform reason design sweater hulking addition lumpy").split( )

play_again = True
while play_again:
  
  chosen_word = random.choice(word_list)
  num_lives = 6
  hashed_word = hash_word(chosen_word)
  print ("Welcome to the hangman game where you have to guess the word. You can start of by guessing a single letter or the whole word if you know what it is. You have {} lives. ".format(num_lives))

  game_over = False
  guesses = []
  alphabet = ("a b c d e f g h i j k l m n o p q r s t u v w x y z").split()
  while not game_over:

    print ("The word that you are guessing is {}, you have {} guesses left.".format(hashed_word, num_lives))
    show_alphabet(alphabet)

    user_guess = good_valid_guess(guesses)

    if user_guess in alphabet:
      alphabet[alphabet.index(user_guess)] = '#'

    #Parameters for correct guess
    # game_over = parameters_word_chosen(chosen_word, user_guess)

    #User guessed a correct letter
    if user_guess in chosen_word and len(user_guess) == 1:
      guesses.append(user_guess)
      indexes = []
      for k in range (len(chosen_word)):
        if user_guess == chosen_word[k]:
          indexes.append(k)
      # print(indexes)
      for c in range(len(indexes)):
        hashed_word = list(hashed_word)
        hashed_word[indexes[c]] = user_guess
        hashed_word = "".join(hashed_word)
    elif chosen_word == user_guess:
      game_over = True
    else:
      guesses.append(user_guess)
      num_lives -= 1

    if hashed_word == chosen_word or num_lives < 1:
      game_over = True


  win_conditions(num_lives)
  
  play_again = input("\nWould you like to play again? (Y/N): ").lower() == 'y'
  

  