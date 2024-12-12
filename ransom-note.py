# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed
# by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map_of_available_characters = {key: 0 for key in magazine}
        for c in magazine:
            map_of_available_characters[c] += 1
        for c in ransomNote:
            if map_of_available_characters.get(c, 0) >= 1:
                map_of_available_characters[c] -= 1
            else:
                return False
        return True
