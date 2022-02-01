n=int(input(""))
a=(input(""))
b=(input(""))

n1=-1

a2=a.split()
b2=b.split()

a3=0
b3=0



for i in range(n):
  n1+=1
  if a2[n1]== "rock":
    if b2[n1]=="paper":
      b3+=1
    elif b2[n1]=="scissors":
      a3+=1
    elif b2[n1]=="rock":
      continue
  if a2[n1]== "paper":
    if b2[n1]=="scissors":
      b3+=1
    elif b2[n1]=="rock":
      a3+=1
    elif b2[n1]=="paper":
      continue

  if a2[n1]== "scissors":
    if b2[n1]=="rock":
      b3+=1
    elif b2[n1]=="paper":
      a3+=1
    elif b2[n1]=="scissors":
      continue


print(a3,b3)
