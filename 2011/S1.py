line=int(input(""))
t,s = 0,0
for i in range(line):
  text=input("")
  e=text.lower()
  t+=e.count("t")
  s+=e.count("s")
 
if t>s:
  print("English")
elif t<s:
  print("French")
elif t==s:
  print("French")
