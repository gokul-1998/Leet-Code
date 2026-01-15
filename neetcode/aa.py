class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={'{':"}","[":']',"(":")"}
        for i in s:
            if i in pairs:
                stack.append(i)
            else:
                if not stack:
                     return False
                top=stack.pop()
                if i != pairs[top]:
                    return False
        return not bool(stack)
    
# cases to think : 
    