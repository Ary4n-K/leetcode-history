class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(x,n):
            return chr(ord(x)+int(n))
        l = len(s)
        res = list(s)
        for i in range(l):
            if i%2 != 0:
                res[i] = shift(s[i-1], s[i])
        a = ''.join(res)        
        return a
