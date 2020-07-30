n=int(input())
maxx=1
for _ in range(n):
  x=int(input())
  if x%2!=0:
    if x>maxx:
      maxx=x
print("Largest odd number",maxx)