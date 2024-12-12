# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced
# with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replacements = {}
        replacements_inverse = {}
        for _s, _t in zip(s, t):
            if _s in replacements:
                if _t != replacements[_s]:
                    return False
            else:
                replacements[_s] = _t
                if _t in replacements_inverse:
                    if replacements_inverse[_t] != _s:
                        return False
                else:
                    replacements_inverse[_t] = _s
        return True


print(Solution().isIsomorphic("badc", "baba"))
