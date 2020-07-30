x=str(input())
print("Captial=",x.capitalize())
print("Maxiumum letter=",max(x))
print("Minumum=",min(x))
print("Lowercase=",x.islower())
print("Uppercase=",x.isupper())
print("Digit=",x.isdigit())

import base64 
  

sample_string_bytes = x.encode("ascii") 
  
base64_bytes = base64.b64encode(sample_string_bytes) 
base64_string = base64_bytes.decode("ascii") 
  
print(f"Encode {base64_string}")

print()
print("Decode=",x)
