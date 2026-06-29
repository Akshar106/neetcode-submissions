class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_string_s = ''.join(sorted(s))
        sorted_string_t = ''.join(sorted(t))
        if len(s) != len(t):
            return False
        for i in range (0,len(s)):
            if sorted_string_s[i] != sorted_string_t[i]:
                return False
        return True