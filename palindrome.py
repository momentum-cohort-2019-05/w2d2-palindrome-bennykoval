user_sentence = input("Write whatever you'd like: ")
all_letters = "abcdefghijklmnopqrstuvwxyz"
found_letters = []
found_letters_backwards = []

def return_backwards(x):
  """Return text user inputs in backwards form, store return in new variable"""   
  return x[::-1]

user_sentence_backwards = return_backwards(user_sentence)

for letter in user_sentence.lower():
    if letter in all_letters and letter not in found_letters:
        found_letters.append(letter)

for letter in user_sentence_backwards.lower():
    if letter in all_letters and letter not in found_letters_backwards:
        found_letters_backwards.append(letter)


if found_letters == found_letters_backwards:
    print((user_sentence), "is a palindrome")
else:
    print((user_sentence), "is not a palindrome")
