N=int(input("Enter a number: "))
isPrime=True
i=2
while i<=N/2:
     if N%i==0: continue
     else:
         isPrime=False
         break
i+=1
print(isPrime)