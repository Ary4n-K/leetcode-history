class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=''
        for i in s:
            if i.isalpha():
                a+=i.lower()
            elif i.isnumeric():
                a+=i
        if a==a[::-1]:
            return True
        return False
                
