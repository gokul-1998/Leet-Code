x=[-2,0,3,-5,2,-1]

def prefix_sum(x):
    return [x[i] if i==0 else x[i]+x[i-1]  for i in range(len(x))]

print(prefix_sum(x))