def isStringPermutation(s1, s2): #assuming strings are the same length
    count = 0 
    
    for char in s1:
        
        if char in s2:
            count += 1

    return count == len(s1) 
    
    


def pairsThatEqualSum(intlist, targ):
    targlist = []
    
    for num1 in intlist: #checks all possible sum pairs in nested for loop
    
        for num2 in intlist:
            
            if num1 + num2 == targ and targlist.count((num1,num2)) == 0: #no duplicates
                targlist.append((num1, num2))
                
    return targlist
