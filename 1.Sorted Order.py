lst=[]
while True:
  x=int(input())
  if x==0:
    break
  else:
    lst.append(x)
    
lst.sort()
for i in lst:
  print(i)
    