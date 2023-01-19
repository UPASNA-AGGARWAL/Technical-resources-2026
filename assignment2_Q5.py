n=int(input("Enter no. of rows"))
for i in range(n):
  print(""*(row-i)+"*"*(i+1))
for j in range(n-1):
  print(""*(j+2)+"*"*(n-1-j))
    
