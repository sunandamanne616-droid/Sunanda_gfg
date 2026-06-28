class Solution:
    def areAnagrams(self, s1, s2):
        # code here
        if len(s1) != len(s2):
            return False
        return sorted(s1) == sorted(s2)