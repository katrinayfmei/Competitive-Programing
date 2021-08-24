x = int(input())
a = ""
for i in range(x):
  y = input().split(" ")
  a += y[1]*int(y[0])+"\n"
print(a)
