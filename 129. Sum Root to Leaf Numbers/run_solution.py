# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, path_sum):
            if not node:
                return 0
            path_sum = path_sum * 10 + node.val
            if not node.left and not node.right:
                return path_sum
            return dfs(node.left, path_sum) + dfs(node.right, path_sum)
        
        return dfs(root, 0) 
    
def create_tree(x):
    root = TreeNode(x[0])
    q = deque([root])
    i = 1
    while i < len(x):
        node = q.popleft()
        if x[i] is not None:
            node.left = TreeNode(x[i])
            q.append(node.left)
        i += 1
        if i < len(x) and x[i] is not None:
            node.right = TreeNode(x[i])
            q.append(node.right)
        i += 1
    return root

# Test the function
def test():
    solution = Solution()
    x=[1,2,3]
    root = create_tree(x)
    assert solution.sumNumbers(root) == 25
    
    x=[4,9,0,5,1]
    root = create_tree(x)
    assert solution.sumNumbers(root) == 1026
    print('All tests passed')

if __name__ == '__main__':
    test()
    