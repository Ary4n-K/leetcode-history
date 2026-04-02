class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s).most_common()
        a=''
        l=[]
        for i in c:
            l.append(i[0]*i[1])
        return ''.join(l)    
