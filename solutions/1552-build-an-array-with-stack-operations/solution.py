class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        l = []
        r = []
        for i in range(1,n+1):
            l+=[i]
            r+=["Push"]
            if l==target:
                return r
                break
            if i not in target:
                r+=["Pop"]   
                l.pop() 
        return r   
