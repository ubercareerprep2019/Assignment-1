def isStringPermutation(s1, s2):
    s1set = set(s1)
    x = 0
    for char in s2:
        if char in s1set:
            x += 1
    
    return x == len(s2)
    
    


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
