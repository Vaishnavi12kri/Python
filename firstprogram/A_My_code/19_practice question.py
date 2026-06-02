

A = int(input("A : "))
G = input("M/F : ").upper()
if(A == 1 or A == 2) and G == "M":
  print("fee is 100")
elif(A == 3 or G == "F"):
  print("fee is 200")
elif(A == 5 and G == "M"):
  print("fee is 300")
else:
  print("no fee")
