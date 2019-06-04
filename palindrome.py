user_sentence = input("Enter a sentence or two: ")
all_letters = "abcdefghijklmnopqrstuvwxyz"
found_letters = []
found_letters_backwards = []

def return_backwards(x): 
  return x[::-1]

user_sentence_backwards = return_backwards(user_sentence)

print(user_sentence_backwards)

for letter in user_sentence.lower():
    if letter in all_letters and letter not in found_letters:
        found_letters.append(letter)

for letter in user_sentence_backwards.lower():
    if letter in all_letters and letter not in found_letters_backwards:
        found_letters_backwards.append(letter)


if found_letters =
#if user_sentence is user_sentence[::-1]:
    #print("is a palindrome")
#else:
    #print("is not a palindrome")
        
#print(found_letters)
#print(sorted(found_letters))
