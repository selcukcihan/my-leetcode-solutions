from typing import List

# Given n non-negative integers representing an elevation map
# where the width of each bar is 1,
# compute how much water it can trap after raining.


class Solution:
    def __init__(self, debug=False):
        self.debug = debug

    def _print(self, str):
        if self.debug:
            print(str)

    def trap(self, height: List[int]) -> int:
        # start from the left and scan to the right, at each iteration
        # draw a line to the right,
        #   if it intersects the heights jump to that position and count how much water it trapped
        #   if it doesn't intersect, crawl down one position and try, repeat until you hit a height
        trapped_water = 0
        current_horizontal_position = (
            0  # index into height array, represents the horizontal position
        )
        current_vertical_position = 0  # current height the scan line sits at
        while current_horizontal_position < len(height):
            self._print(f"horizontal at {current_horizontal_position}")
            # ascending, if there is a hill we need get past
            while current_vertical_position < height[current_horizontal_position]:
                current_vertical_position += 1

            self._print(f"scan line starts at vertical {current_vertical_position}")
            scan_line_hit = False
            # this is where we shoot horizontal lines and try to hit a height
            # at each iteration we'll try to hit a height, if not ve reduce current_v and try again
            while current_vertical_position >= 0:
                scan_line_end_index = -1
                self._print(f"shoot at height {current_vertical_position}")
                for col in range(current_horizontal_position + 1, len(height)):
                    if height[col] >= current_vertical_position:
                        scan_line_end_index = col
                        self._print(f"scan line hit at {scan_line_end_index}")
                        break

                if scan_line_end_index >= 0:
                    # calculate trapped water:
                    #   height of the line is current_vertical_position
                    #   do calculation within the range (current_horizontal_position, scan_line_end_index)
                    #   note that the end points are not included
                    trapped_water += self._calculate_trapped_water(
                        height,
                        current_vertical_position,
                        current_horizontal_position + 1,
                        scan_line_end_index - 1,
                    )
                    current_horizontal_position = scan_line_end_index
                    scan_line_hit = True
                    break
                else:
                    # move the scan line one level below (descending)
                    current_vertical_position -= 1

            if not scan_line_hit:
                current_horizontal_position += 1
        return trapped_water

    def _calculate_trapped_water(
        self, height: List[int], vertical_position, start, end
    ):
        trapped_water = 0
        self._print(f"trapping water between [{start}, {end}]")
        for h in height[start : end + 1]:
            assert vertical_position - h >= 0
            trapped_water += vertical_position - h
        return trapped_water


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# print(Solution().trap([1, 0, 0, 1, 3, 0, 2, 1, 0, 0]))
print(Solution().trap([0, 1, 0, 1]))
print(Solution(True).trap([4, 2, 0, 3, 2, 5]))
