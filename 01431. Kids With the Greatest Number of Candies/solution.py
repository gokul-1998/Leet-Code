## my solution
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_all=max(candies)
        op=[]
        for i in candies:
            op.append(i+extraCandies>=max_all)
        return op


## better solution
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_all = max(candies)
        return [(candy + extraCandies) >= max_all for candy in candies]
