# 1095. Find in Mountain Array
# https://leetcode.com/problems/find-in-mountain-array/description/


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Step 1: find peak
        def peak_in_mountain_array(arr):
            start, end = 0, arr.length() - 1
            while start < end:
                mid = (start + end) // 2
                mid_val = arr.get(mid)
                next_val = arr.get(mid + 1)
                if mid_val < next_val:
                    start = mid + 1
                else:
                    end = mid
            return start

        # Step 2: binary search in a given order
        def binary_search(arr, target, start, end, ascending=True):
            while start <= end:
                mid = (start + end) // 2
                mid_val = arr.get(mid)
                if mid_val == target:
                    return mid
                if ascending:
                    if mid_val < target:
                        start = mid + 1
                    else:
                        end = mid - 1
                else:
                    if mid_val < target:
                        end = mid - 1
                    else:
                        start = mid + 1
            return -1

        # main
        peak = peak_in_mountain_array(mountainArr)

        # search left (ascending)
        ans = binary_search(mountainArr, target, 0, peak, True)
        if ans != -1:
            return ans

        # search right (descending)
        return binary_search(mountainArr, target, peak + 1, mountainArr.length() - 1, False)
