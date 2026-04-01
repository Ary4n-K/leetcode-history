class Solution:
    def reverseWords(self, s: str) -> str:
        ps=''
        l= s.split()      
        for i in l:
            ps+=(i[::-1])+' '
        return ps.rstrip()
