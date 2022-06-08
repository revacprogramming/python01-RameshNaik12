# Object Oriented Programming
# https://www.py4e.com/lessons/Objects
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
if a>b and b>c:
  print(f"{a} is the largest number")
elif b>=a and b>=c:
  print(f"{b} is largest number")
else:
  print(f"{c} is largest number")