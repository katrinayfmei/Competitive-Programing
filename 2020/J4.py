t=str (input(""))
s=str (input(""))
k = list(map(str, s))

m="no"
for n in k[::-1]:
  #remove last of the list
  k.pop(-1)
  #Placing the last element of list to the front
  k.insert(0,n)
  result = ''.join(map(str,k)) 
  if result in t:
    m="yes"
    break
print(m)
