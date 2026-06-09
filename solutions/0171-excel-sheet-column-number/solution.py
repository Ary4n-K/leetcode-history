class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        t = 0            
        for i in columnTitle:
            n = ord(i) - 64
            t = t*26 + n
        return t    
