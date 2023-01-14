num1=int(input())
num2=int(input())
if num1>num2:
  greater= num1
else:
  greater= num2
while=True:
  if greater%num1==0 and greater%num2==0:
    LCM=greater
    break
  greater+=1
  print("LCM:",LCM)
while(num2):
  num1,num2=num2,num1%num2
  print("GCD:"<num1)
