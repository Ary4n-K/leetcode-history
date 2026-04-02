class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l=[]
        a=[]
        for i in arr1:
            if i not in arr2:
                a.append(i)
        for i in arr2:
            for j in arr1:
                if j == i:
                    l.append(j)
                   
        return l+sorted(a)            

