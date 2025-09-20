# 33. Search in Rotated Sorted Array

# - https://leetcode.com/problems/search-in-rotated-sorted-array/description/
import re
from typing import List
# def search( nums: List[int], target: int) -> int:
def findpivot(arr):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=start+(end-start)//2
        # 4 cases
        # case 1: 
        if mid < end and arr[mid]>arr[mid+1]: # 3 4 5 1 2 , mid<end(because in case mid is last element of array, it will throw error)
            return mid
        if mid > start and arr[mid]<arr[mid-1]: # 4 5 1 2 3
            return mid-1

        if arr[mid]<=arr[start]: #3,4,5,1,2 all elements after the mid element are going to be smaller than the start., ignore all the elements from middle
            end=mid-1
        else:
            start=mid+1
    return -1

def binarysearch(lis,target,start,end):
    while start<=end:
        mid=start + (end-start)//2
        if lis[mid]==target:
            return mid
        elif lis[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return -1

def rotated_array_binarysearch(lis,target):
    pivot=findpivot(lis)
    # if we did not find a pivot , it means the array is not rotated,just do normal binary search.
    if pivot==-1:
        return binarysearch(lis,target,0,len(lis)-1)
    # if pivot is found, you have found two ascending sorted arrays
    if lis[pivot]==target:
        return pivot
    
    if target >= nums[0]:
        return binarysearch(lis,target,0,pivot-1)
    
    return binarysearch(lis,target,pivot+1,len(lis)-1)


# we have 3 cases, 1) pivot = target, 
#                  2) target > start  || search for 6 , search space = (s,p-1), because all number after pivot are smaller than start.
#                  3) else search in the remaining, target <  start,then we know that all the elem between s and pivot is
#                     going to be bigger than target, eg target=1, search space = (p+1,e)


    # lets say if target is 6,
lis=[4,5,6,7,0,1,2] 

print(findpivot(lis))
