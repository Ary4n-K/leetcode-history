class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        c = 0
        for i in s:
            if (chr(ord(i)+32) in s) :
                c+=1
        return c    
