# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed
# from the original string by deleting some (can be none) of
# the characters without disturbing the relative positions of
# the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        _t = -1
        for _s in range(len(s)):
            found = False
            while _t < len(t) - 1:
                _t += 1
                if t[_t] == s[_s]:
                    found = True
                    break
            if not found:
                return False
        return True


print(Solution().isSubsequence("ace", "abcde"))
print(Solution().isSubsequence("aec", "abcde"))
