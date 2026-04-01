class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s= set(sentence)
        a=set('abcdefghijklmnopqrstuvwxyz')
        if s==a:
            return True
        return False    
