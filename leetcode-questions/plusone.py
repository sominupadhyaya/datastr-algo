

def plusOne(digits):
    string = ""
    
    final_arr = []
   
    for i in digits:
        string += str(i)    
        res = str(int(string) + 1)
    
    for k in res:
        final_arr.append(int(k))
    
    print(final_arr)

plusOne([9,9,9,9,9])