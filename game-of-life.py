from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dup = [[x for x in row] for row in board]

        def get_live_neighbor_count(row, col):
            count = 0
            if row - 1 >= 0:
                count += dup[row - 1][col]
            if row - 1 >= 0 and col + 1 < len(dup[0]):
                count += dup[row - 1][col + 1]
            if col + 1 < len(dup[0]):
                count += dup[row][col + 1]
            if row + 1 < len(dup) and col + 1 < len(dup[0]):
                count += dup[row + 1][col + 1]
            if row + 1 < len(dup):
                count += dup[row + 1][col]
            if row + 1 < len(dup) and col - 1 >= 0:
                count += dup[row + 1][col - 1]
            if col - 1 >= 0:
                count += dup[row][col - 1]
            if row - 1 >= 0 and col - 1 >= 0:
                count += dup[row - 1][col - 1]
            # print(f"calc: [{row},{col}] => {count}")
            return count

        for row in range(len(board)):
            # print(f"row: {row}")
            for col in range(len(board[row])):
                count = get_live_neighbor_count(row, col)
                # print(f"col {col} has {count}")
                current = dup[row][col]
                if current == 1 and count < 2:
                    board[row][col] = 0
                elif current == 1 and count > 3:
                    board[row][col] = 0
                elif current == 0 and count == 3:
                    board[row][col] = 1


Solution().gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
