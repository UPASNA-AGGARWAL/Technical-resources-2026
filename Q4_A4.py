low=int(input("Enter low range:"))
high=int(input("Enter high range:"))
for i in range(low,high+1):
  prime=1
  for j in range(2,i):
    if i%j==0:
      prime=0
      break
  if prime==1:
    print(i)
