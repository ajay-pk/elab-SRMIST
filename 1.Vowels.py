def count_v(string): 
    count=0
    vowels = ('a', 'e', 'i', 'o', 'u')  
    for x in string.lower(): 
        if x in vowels: 
          count+=1
    print("Number of vowels are")
    print(count)
            
count_v(str(input()))