n1=int(input())
n2=int(input())
lst1=[]
lst2=[]
for _ in range(n1):
  lst1.append(int(input()))
for _ in range(n2):
  lst2.append(int(input()))

lst1.extend(lst2)
print("The Extended List")
print(lst1)
print("The Reverse List")
lst1.reverse()
print(lst1)
lst1.remove(int(input()))
print(lst1)
              
              
              
              