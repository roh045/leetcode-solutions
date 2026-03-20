class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        rows = [""] * numRows
        curr_row = 0
        direction = -1

        for char in s:
            rows[curr_row] += char

            # change direction at top/bottom
            if curr_row == 0 or curr_row == numRows - 1:
                direction *= -1

            curr_row += direction

        return "".join(rows)