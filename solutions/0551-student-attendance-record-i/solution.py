class Solution:
    def checkRecord(self, s: str) -> bool:
        d=Counter(s)
        return  (d["A"]<2) and ('LLL' not in s)
