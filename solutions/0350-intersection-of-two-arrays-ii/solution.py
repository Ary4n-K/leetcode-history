class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1
        c = Counter(nums1) 
        res = []
        for i in nums2:
            if c.get(i,0)>0:
                res.append(i)
                c[i]-=1
        return res         
