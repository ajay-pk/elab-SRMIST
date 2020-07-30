x=int(input())
y=int(input())
lst=[]
for i in range(x,y+1):
  if i%2==0:
    lst.append(i)
print(lst)