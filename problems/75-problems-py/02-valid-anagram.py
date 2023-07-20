def isAnagram(s, t):
    if len(s) != len(t):
        return False
    alphaChecks = [0]*26
    for x in s:
        alphaChecks[ord(x) - 97] += 1
    
    for x in t:
        if alphaChecks[ord(x) - 97] != 0:
            alphaChecks[ord(x) - 97] -= 1
        else:
            return False
    for x in alphaChecks:
        if x > 0:
            return False 
    return True