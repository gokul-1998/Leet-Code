# find_the_smallest_number_that_is_greater_than_or_equal_to_the_given_number
# target will always be within the extremes, so dont check for 19

lis=[2,3,5,9,14,16,18]

def search(lis,target):
    start=0
    end=len(lis)-1
    while start<=end:
        mid=start+(end-start)//2
        print(lis,target,start,mid,end)
        if target==lis[mid]:
            return mid
        
        if lis[mid]<target: # 9>=4, end=[2],start=[2],mid=[1]
            start=mid+1
        else:
            end=mid-1
    print()
    return start

        

assert search(lis,5)==2

assert search(lis,4)==2

assert search(lis,16)==5
print("done")