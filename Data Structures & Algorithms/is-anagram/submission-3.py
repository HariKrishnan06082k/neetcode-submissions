class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {} 
        t_dict = {}

        if len(s) != len(t):
            return False
        
        for c in range(len(s)):
            s_dict[s[c]] = 1 + s_dict.get(s[c],0)
            t_dict[t[c]] = 1 + t_dict.get(t[c],0)
        for s in s_dict:
            if s_dict[s] != t_dict.get(s,0):
                return False
        return True
