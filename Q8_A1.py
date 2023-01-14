n=int(input("Enter no."))
t=0
k=int(n%10)
n=int(n/10)
x=1
while n>0:
  rem=int(n%10)
  n=int(n/10)
  n+=rem*x
  x*=10
