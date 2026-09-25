S=input("Enter a sentence: ")
W=input("Enter a word: ")

words=S.split()
count=0
for i in words:
    if i==W:
        count+=1
    print("Occurence : ",count)