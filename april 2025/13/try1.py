
import itertools

def get_permutations(s):
    return [''.join(p) for p in itertools.permutations(s)]

def get_dist_palindromes(s,k):
    lis=[]
    if len(s)%2==0:
        for i in get_permutations(s[:len(s)//2]):
            lis.append(i+i[::-1])
    else:
        for i in get_permutations(s[:len(s)//2]):
            lis.append(i+s[len(s)//2]+i[::-1])
    try:
        # because permutations contains duplicates
        return sorted(list((set(lis))))[k-1]
    except:
        return ""
 
s="aabbaa"
s="ijlnrdismkkmsidrnlji"
# 288371
k=2
print(get_dist_palindromes(s,2))