texts=input("enter a word:")
texts=texts.lower()
reversed_texts=texts[::-1]
if texts==reversed_texts:
    print({texts:"palindrome"})
else:print({texts:" not palindrome"})