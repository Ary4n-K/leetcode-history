class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if (s2 == s1[2]+s1[1]+s1[0]+s1[3]) or (s2== s1[0]+s1[3]+s1[2]+s1[1]) or (s2== s1[2]+s1[3]+s1[0]+s1[1]) or (s2==s1):
            return True
        return False    
