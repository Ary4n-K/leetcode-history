class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split()
        if len(pattern) != len(l):
            return False
        d = {}
        seen_words = set()  
        for c, w in zip(pattern, l):
            if c in d:
                if d[c] != w:
                    return False
            else:
                if w in seen_words:
                    return False
                    
                seen_words.add(w)
                d[c] = w
                
        return True                             
