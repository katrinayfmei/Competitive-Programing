n=int(input(""))
xL=[]
yL=[]

for i in range(n):
  x,y=(input()).split(",")
  xL.append(int(x))
  yL.append(int(y))

blx=(min(xL))-1
bly=(min(yL))-1

tlx=(max(xL))+1
tly=(max(yL))+1

print(str(blx) +"," + str(bly))
print(str(tlx) +"," + str(tly))
