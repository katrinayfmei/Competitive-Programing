sign = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']
a = input("")
b = True
for i in range(0, len(a)):
  if a[i] not in sign:
    b = False
    print("NO")
    break

if b:
  print("YES")
