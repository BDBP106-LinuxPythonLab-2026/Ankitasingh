letters=input("Enter a string: ")
letters=letters.lower()
vowels=['a','e','i','o','u']
if letters in vowels:
    print({letters:"vowel"})
else:print({letters:"consonants"})
