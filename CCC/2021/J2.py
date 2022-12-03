n=int(input(""))
p=[]
l=[]
for i in range(n):
  a=str(input(""))
  b=int(input(""))
  p.append(a)
  l.append(b)

hold=0

for i in range(len(l)):
  if l[i]>hold:
    hold=l[i]
  else:
    continue


ind=l.index(hold)

print(p[ind])
