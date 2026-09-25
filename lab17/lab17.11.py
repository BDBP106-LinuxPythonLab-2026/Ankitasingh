L=[1,2,2,3,5,6,7,8]
j=2
for i in range (1,len(L)):
    for j in range (i+1,len(L)):
        if L[i]==L[j]:
            print('numbers are: ',L[j])