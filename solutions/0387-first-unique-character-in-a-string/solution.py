class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=Counter(s)
        n=0
        for i in d:
            if d[i]==1:
                n=i
            for i in range(len(s)):
                if s[i]==n:
                    return i
        return -1
