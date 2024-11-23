https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

```
1071. Greatest Common Divisor of Strings
Easy
Topics
Companies
Hint
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
```

## approach
- Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
- 


## best solution
```python
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        # the below condition is to check if the two strings are equal or not
        # this is important because, it is given in the question that s=t+t+t+t+...+t
        # which means , in second example, ABABAB = AB + AB + AB,
        #= ABAB= AB + AB
        # we cannot get ABAB as gcd, as you cannot add ABAB to get ABABAB
        # so the logic to check is that if they are not palindrome, they dont have a gcd
        if str1 + str2 != str2 + str1:
            return ""
        # this is the key part, if the length of str1 is equal to str2, then return str1

        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])
```

