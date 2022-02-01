a=int(input(""))
b=int(input(""))
c=int(input(""))
d=int(input(""))

if a == 1:
  total=461
elif a == 2:
  total=431
elif a == 3:
  total=420
else:
  total=0



if b == 1:
  total+=100
elif b == 2:
  total+=57
elif b == 3:
  total+=70
else:
  total+=0

if c == 1:
  total+=130
elif c == 2:
  total+=160
elif c == 3:
  total+=118
else:
  total+=0

if d == 1:
  total+=167
elif d == 2:
  total+=266
elif d == 3:
  total+=75
else:
  total+=0



print("Your total Calorie count is "+ str(total) + ".")
