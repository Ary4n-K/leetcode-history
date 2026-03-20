class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=1
        cmax=1
        c1=0
        for i in range(len(nums)):
            if nums[i]==1:
                c1+=1
        if c1==0:
            return 0        
        for i in range(1,len(nums)):
            if nums[i]==1 and nums[i-1]==1:
                c+=1
                if c>cmax:
                    cmax=c
            else: c=1

        return cmax
