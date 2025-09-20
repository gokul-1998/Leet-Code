x=[1,2,3,4,5]
y=[5,4,3,2,1]


def search(lis,target):
    start=0
    end=len(lis)-1
    while start<=end:
        mid=start+(end-start)//2
        if lis[mid]==target:
            return mid
        if lis[0]>lis[-1]:
            if lis[mid]<target:
                end=mid-1
            else:
                start=mid+1
        else:
            if lis[mid]<target:
                start=mid+1
            else:
                end=mid-1



assert search(x,2)==1
assert search(y,2)==3
print("done")