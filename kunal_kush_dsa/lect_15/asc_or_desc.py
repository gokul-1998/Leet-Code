x=[3,3,3,3,3,4]


def is_asc(x):
    return x[0]<x[-1]


assert is_asc([1,2,3,4])==True
assert is_asc([14,12,11,4])==False
print("done")