n1 = float(input("number 1 "))
op = int(input("what operation?\n1.multiplication\n2.substraction\n3.addition\n4.division\n"))
n2 = float(input("number 2 "))
if op == 1:
  print("result is", n1*n2)
elif op == 2:
  print("result is",  n1+n2)
elif op == 3:
  print("result is", n1-n2)
elif op == 4:
  print("result is", n1/n2)
else:
  print('does not exist')