x=str(input())
y=str(input())
if len(x)==len(y):
  print("Both strings are equal")
elif len(x)>len(y):
  print("Larger string is:")
  print(x)
elif len(y)>len(x):
  print("Larger string is:")
  print(y)