# find peak in mountain array and return it's index


lis=[1,2,3,4,5,6,4,3,2]

def mountain_array(lis):
    start=0
    end=len(lis)-1
    while start<end:
        mid=start+(end-start)//2
        if lis[mid]>lis[mid+1]:
            end=mid
        else:
            start=mid+1
    return start 