# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection
# between a letter in pattern and a non-empty word in s. Specifically:
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mappings = {}
        inverse_mappings = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        for p, word in zip(pattern, words):
            if p not in mappings:
                if word in inverse_mappings:
                    return False
                mappings[p] = word
                inverse_mappings[word] = p
            else:
                if mappings[p] != word:
                    return False
        return True
