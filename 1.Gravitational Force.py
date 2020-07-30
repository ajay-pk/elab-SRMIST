def calculate_g(m1,m2,r):
  G=6.673*(10**-11)
  f=(G*m1*m2)/(r**2)
  if f<105:
    print("{:.2f}".format(f),"N")
  else:
    print("105.1 N")
calculate_g(int(input()),int(input()),int(input()))