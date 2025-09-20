x=[10,8,7,4,2,1,-1]
from typing import List

def search( nums: List[int], target: int) -> int:
    start=0
    end=len(nums)-1
    while start<=end:
        mid=start+(end-start)//2
        if nums[mid]==target:
            return mid
        if nums[mid]<target:
            end=mid-1
        else:
            start=mid+1
    return -1


assert search(x,8)==1
assert search(x,1)==5
assert search(x,100)==-1
print("done")
