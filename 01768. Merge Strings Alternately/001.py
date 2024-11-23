## Blind solution

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        op=""
        while i < len(word1) and i < len(word2):
            op+=word1[i]
            op+=word2[i]
            i+=1
        if len(word1)>len(word2):
            op+=word1[i:]
        else:
            op+=word2[i:]
        return op

## better  solutions

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        l = min(len(word1),len(word2))
        for i in range(l):
            output += word1[i] + word2[i]
        if len(word1)>l:
            output += word1[l:]
        if len(word2)>l:
            output += word2[l:]
        return output


## Another solution
# using zip
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(a+b for a,b in zip_longest(word1,word2,fillvalue=''))



## aadhi's solution

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) > len(word2):
            ans = ''.join(a+b for a,b in zip(word1,word2)) + word1[len(word2):]
        elif len(word1) < len(word2):
            ans = ''.join(a+b for a,b in zip(word1,word2)) + word2[len(word1):]
        else:
            ans = ''.join(a+b for a,b in zip(word1,word2))
        return ans
    