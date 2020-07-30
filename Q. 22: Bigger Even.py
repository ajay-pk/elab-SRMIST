l=int(input())
lst=[]
for i in range(l):
  x=int(input())
  if x%2==0:
    lst.append(x)
print("Largest even number:",max(lst))