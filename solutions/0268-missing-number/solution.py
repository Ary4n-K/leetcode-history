class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l =[i for i in range(len(nums)+1)]
        n= set(l)-set(nums)
        for i in n:
            return i
