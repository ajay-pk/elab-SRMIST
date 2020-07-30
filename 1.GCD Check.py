def hcfnaive(a,b): 
    if(b==0): 
        return a 
    else: 
        return hcfnaive(b,a%b) 
  
a= int(input())
b= int(input())

print ("The GCD of the two numbers is ",end="") 
print (hcfnaive(a,b)) 