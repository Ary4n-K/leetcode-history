class Solution:
    def addDigits(self, num: int) -> int:
        res = 99
        while res>=10:
            s = str(num)
            res = sum (int(i) for i in s)
            num = res
        return res  

