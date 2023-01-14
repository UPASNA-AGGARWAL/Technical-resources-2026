marks=int(input("Enter marks :"))
if marks>90:
  print("EXCELLENT")
elif marks>80 or marks<90:
  print("GOOD")
elif marks>70 or marks<80:
  print("FAIR")
elif marks>60 or marks<70:
  print("MEETS EXPECTATIONS")
else:
  print("BELOW PAR")
