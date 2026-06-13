class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        c=0
        print(expected)
        l = len(heights)
        for i in range(l):
            if expected[i] != heights[i] :
                c+=1
        return c        
