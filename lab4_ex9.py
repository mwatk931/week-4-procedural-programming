first_word = input("Enter a word: ").lower()
second_word = input("Enter another word: ").lower()

first_letters = list(first_word)
second_letters = list(second_word)

if sorted(first_letters) == sorted(second_letters):
    print("The words are anagrams.")
else: 
    print("The words are not anagrams.")