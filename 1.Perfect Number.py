def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
if perfect_number(int(input())):
  print("The number is a Perfect number!")
else:
  print("The number is not a Perfect number!")
  
