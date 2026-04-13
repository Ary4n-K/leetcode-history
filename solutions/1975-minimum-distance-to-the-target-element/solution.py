class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        b=[]
        l=len(nums)
        for i in range(l):
            if nums[i]== target :
                j=abs(i - start)
                b.append(j)
        return min(b)    
