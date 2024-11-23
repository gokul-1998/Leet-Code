## my solution
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_all=max(candies)
        for i in candies:
            op.append(i+extraCandies>=max_all)
            
        return op

