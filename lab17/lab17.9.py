def if_anagrams(str1, str2, clean=None):
     clean.str1=str1.replace(" ","").lower()

     clean.str2=str2.replace(" ","").lower()
     return clean.str1==clean.str2
word1=input("enter first word")
word2=input("enter second word")
if if_anagrams(word1,word2):
    print('{} and {} are anagrams')