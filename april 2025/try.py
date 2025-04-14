x="daccad"

# def small_pal(x):
#     y=sorted(x)
#     op=""
#     for i in range(0,len(y),2):
#         op+=y[i]
#     if len(y)%2==0:
#         op+=op[::-1]
#     else:
#         op+=op[:-1][::-1]
#     return op
#     # wrong because for "yey" i get "eye" , it should be "yey"
from collections import Counter


def small_pal(s):
    freq=Counter(s)
    mid=""
    op=""
    for k in sorted(freq.keys()):
        if freq[k]%2==0:
            op+=freq[k]//2*k
        else:
            op+=freq[k]//2*k
            mid+=k
    if len(s)%2==0:
        op+=op[::-1]
    else:
        op+=mid+op[::-1]
    return op

print(small_pal(x))
