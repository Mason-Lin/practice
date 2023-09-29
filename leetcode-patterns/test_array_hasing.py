from collections import defaultdict


# 36. Valid Sudoku
class Solution36:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        nums = {str(i) for i in range(1, 10)}
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val in nums:
                    if val in rows[r] or val in cols[c] or val in boxes[(r // 3, c // 3)]:
                        return False
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3, c // 3)].add(val)
        return True


def test_36():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert Solution36().isValidSudoku(board) is True


test_36()
