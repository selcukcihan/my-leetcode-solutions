import math


class Solution:
    def _justify(self, words, maxWidth):
        total_spaces = maxWidth - len("".join(words))
        count = len(words) - 1
        if count == 0:
            line = words[0]
            for i in range(len(line), maxWidth):
                line += " "
            return line
        even = math.floor(total_spaces / count)
        more_count = total_spaces - (even * count)
        line = ""
        for idx, word in enumerate(words):
            line += word
            if idx != len(words) - 1:
                for i in range(even):
                    line += " "
                if more_count > 0:
                    line += " "
                    more_count -= 1
        return line

    def fullJustify(self, words, maxWidth):
        current = []
        current_min_length = 0
        lines = []
        while len(words) > 0:
            word = words[0]
            if (
                current_min_length > 0
                and (current_min_length + len(word) + 1) <= maxWidth
            ) or (current_min_length == 0 and len(word) <= maxWidth):
                current.append(word)
                if current_min_length == 0:
                    current_min_length += len(word)
                else:
                    current_min_length += len(word) + 1
                words.pop(0)
            else:
                lines.append(self._justify(current, maxWidth))
                current = []
                current_min_length = 0

        if len(current) > 0:
            line = " ".join(current)
            for i in range(len(line), maxWidth):
                line += " "
            lines.append(line)
        return lines
