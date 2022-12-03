a=int(input(""))
b=int(input(""))
c=int(input(""))

if a+b+c != 180:
  print("Error")

elif a!=b and b!=c and c!=a and a+b+c==180:
  print("Scalene")

elif a+b+c==180 and a==b==c:
  print("Equilateral")

else:
  print("Isosceles")
