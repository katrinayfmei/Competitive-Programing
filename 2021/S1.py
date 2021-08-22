nT=int(input(""))
side= list(map(int, input("").split(" ")))
height= list(map(int, input("").split(" ")))
total=0

for i in range(nT):
  total+=(height[i]*(side[i] + side[i+1]))/2
print(total)
