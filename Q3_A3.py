t=int(input("Enter number of times input to be taken:"))
for i in range(t):
  var=0
  n=int(input("Enter nuber:"))
  for j in range(1,n+1):
    if n%j==0:
      var+1=0
  if var==2:
    print("PRIME NUMBER")
  else:
    print("NOT A PRIME NUMBER")
