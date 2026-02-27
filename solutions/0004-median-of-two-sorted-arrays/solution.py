class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        f=  sorted(nums1+nums2)
        n=int( (len(f)-1)/2)
        
        if len(f)%2==1:
            
            return(f[n])
        else:
            o=int(len(f)/2)
            p=int(len(f)/2-1)
            return((f[o]+f[p])/2)

           
