o = int(input("1) Square \n2) Triangle\n"))
if (o == 1):
  n = int(input("type the length "))
  n = n ** 2
  print(n)
elif (o==2):
  b = int(input("base length "))
  h = int(input("height "))
  n = (b*h)/2
  print(n)
else:
  print("option doesn't exist")