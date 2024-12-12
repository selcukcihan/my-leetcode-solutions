class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_occurences(input: str):
            occurences = {}
            for c in input:
                if c in occurences:
                    occurences[c] += 1
                else:
                    occurences[c] = 1
            return occurences

        if len(s) != len(t):
            return False

        occurences_of_s = get_occurences(s)
        occurences_of_t = get_occurences(t)
        for key in occurences_of_s:
            if occurences_of_s[key] != occurences_of_t.get(key, 0):
                return False

        return True
