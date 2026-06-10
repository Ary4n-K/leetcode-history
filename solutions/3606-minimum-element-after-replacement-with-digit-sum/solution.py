class Solution:
    def minElement(self, nums: List[int]) -> int:
        mn = 99999999
        for i in nums:
            a = sum(int(c) for c in str(i))
            if a<mn:
                mn = a
        return mn        
