string=str(input())
lst=list(map(str,string.split()))
lst.sort()
print("The sorted words are")
for i in lst:
  print(i)
         