class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=nums[n:]
        m=nums[:n]
        g=[]
        for i in range(0,n):
            g=g+[m[i]]
            g=g+[l[i]]
        return g    
