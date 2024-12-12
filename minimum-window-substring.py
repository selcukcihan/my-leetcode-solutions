# Given two strings s and t of lengths m and n respectively, return the minimum window
# substring of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".
# Answer is guaranteed to be unique.

# s = "ADOBECODEBANC", t = "ABC" => "BANC"
#      A         A
#         B     B
#           C      C
# A:1-11, B:4-10, C:6-13
#
# s = "a", t = "aa" => ""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map_count_of_characters_of_t = {key: 0 for key in t}
        indices_of_characters_of_t_within_s = set()

        indices_of_characters_of_s = {key: [] for key in s}
        for j, _s in enumerate(s):
            indices_of_characters_of_s[_s].append(j)

        for _t in t:
            map_count_of_characters_of_t[_t] += 1
            for j in indices_of_characters_of_s.get(_t, []):
                if j not in indices_of_characters_of_t_within_s:
                    indices_of_characters_of_t_within_s.add(j)

        total_number_of_characters_in_t = len(t)
        if len(indices_of_characters_of_t_within_s) < total_number_of_characters_in_t:
            return ""

        indices_of_characters_of_t_within_s = sorted(
            indices_of_characters_of_t_within_s
        )

        current_number_of_characters = 0
        map_occurences = {key: [] for key in t}
        min_distance = len(s) + 1
        min_left = -1
        min_right = -1
        total_list = []
        for i in indices_of_characters_of_t_within_s:
            character = s[i]
            total_count_of_character = map_count_of_characters_of_t[character]
            occurences = map_occurences[character]
            if len(occurences) < total_count_of_character:
                total_list.append(i)
                current_number_of_characters += 1
            else:
                total_list.remove(occurences[0])
                total_list.append(i)

                occurences.pop(0)
            occurences.append(i)

            if current_number_of_characters == total_number_of_characters_in_t:
                left = total_list[0]
                right = total_list[-1]
                distance = 1 + right - left
                if distance < min_distance:
                    min_distance = distance
                    min_left = left
                    min_right = right
        if min_left >= 0 and min_right >= 0:
            return s[min_left : min_right + 1]
        else:
            return ""


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("a", "aa"))
