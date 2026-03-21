class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s1=(n*(n+1))/2
        s2=sum(nums)
        s3=sum(set(nums))        
        return [s2-s3,int(s1-s3)]
