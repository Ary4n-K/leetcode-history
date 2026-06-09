class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        m = len(haystack)
        for i in range(m):
            if haystack[i] == needle[0]:
                a = haystack[i:i+n]
                if a == needle:
                    return i 
        return -1            

