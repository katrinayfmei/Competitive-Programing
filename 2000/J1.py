#code works but fails dmoj grader due to whitespace errors
weekday,days = input().split()
weekday = int(weekday)
days = int (days)
day = 1

print("Sun Mon Tue Wed Thr Fri Sat")
w1=[]
w2=[]
w3=[]
w4=[]
w5=[]

space=weekday-1
for p in range(space):
  w1.append("   ")

for i in range(1,days+1):
  if len(w1)<7:
 
    w1.append(i)
  elif len(w1)==7 and len(w2)<7:

    w2.append(i)
  elif len(w1)==7 and len(w2)==7 and len(w3)<7:
    w3.append(i)
  elif len(w1)==7 and len(w2)==7 and len(w3)==7 and len(w4)<7:
    w4.append(i)
  elif len(w1)==7 and len(w2)==7 and len(w3)==7 and len(w4)==7 and len(w5)<7:
    w5.append(i)


for j in range(len(w1)):
  if (w1[j])=="   ":
    continue
  elif int(w1[j]) < 10:
    w1[j] = "  "+str(w1[j])

for k in range(len(w2)):
  if int(w2[k]) < 10:
    w2[k] = "  "+str(w2[k])
  elif int(w2[k]) < 15:
    w2[k] = " "+str(w2[k])

for n in range(len(w3)):
  if int(w3[n]) < 22:
    w3[n] = " "+str(w3[n])

for o in range(len(w4)):
  if int(w4[o]) < 29:
    w4[o] = " "+str(w4[o])

for p in range(len(w5)):
  if int(w5[p]) < 32:
    w5[p] = " "+str(w5[p])


print(*w1, sep =" ") 
print(*w2, sep =" ") 
print(*w3, sep =" ") 
print(*w4, sep =" ")
print(*w5, sep =" ")
