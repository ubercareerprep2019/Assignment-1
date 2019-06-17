def isStringPermutation(s1, s2): #assuming strings are the same length
    count = 0 
    
    for char in s1:
        
        if char in s2:
            count += 1

    return count == len(s1) 
    
    


def pairsThatEqualSum(intlist, targ):
    targset = set(intlist)
    targlist = []
    x = 0
    while len(targset) != 0 and x != len(intlist):
        if targ - intlist[x] in targset:
            targlist.append((intlist[x], targ - intlist[x]))
            targset.remove(intlist[x])
            targset.remove(targ - intlist[x])
        x += 1
    return targlist
