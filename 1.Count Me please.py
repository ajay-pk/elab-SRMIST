x=str(input())
count_lower=0
count_upper=0
for i in x:
  if i.isalpha():
      if i.islower():
        count_lower+=1
      elif i.isupper():
        count_upper+=1
    
print(count_lower)
print(count_upper)
