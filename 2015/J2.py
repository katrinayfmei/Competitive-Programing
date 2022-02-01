a=str(input(""))
h=a.count(":-)")
s=a.count(":-(")



if h==0 and s==0:
  print("none")

elif h>s:
  print("happy")

elif s>h:
  print("sad")

elif s==h:
  print("unsure")
