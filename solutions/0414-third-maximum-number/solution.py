class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = sorted(list(set(nums)),reverse=True)
        if len(n)<3:
            return max(n)
        else:
            return n[2]    
