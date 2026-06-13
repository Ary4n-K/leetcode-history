class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rS = s[::-1]
        for i in range(len(s)-1):
            sub = s[i:i+2]
            if sub in rS:
                return True

        return False
