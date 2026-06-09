class Solution:
    def reverseVowels(self, s: str) -> str:
        vows = {'A','E',"I","O","U","a","e","i","o","u"}
        l = list(s)
        left = 0
        right = len(s) -1
        while left<right:
            while left<right and s[left] not in vows:
                left+=1
            while left<right and s[right] not in vows:
                right-=1 
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
        return "".join(l)           
