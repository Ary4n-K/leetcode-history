class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        a= 0
        for c in t:
            if c == s[a]:
                a+=1
                if a == len(s):
                    return True

        return False          

