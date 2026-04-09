class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in digits:
            s+=str(i)
        n= int(s)+1
        return [int(i) for i in str(n)]
        
