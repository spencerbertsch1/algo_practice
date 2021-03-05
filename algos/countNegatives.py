class EasySolution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        """
        Count the negatives from the bottom right to the bottom left,
        then right to left sequentially for each row increasing from
        the bottom.

        This simple solution just checks each element and if it's negative,
        then we add one to the total_num_negatives int value
        """

        total_num_negatives = 0

        for i, row in enumerate(grid):
            for element in row:
                if element < 0:
                    total_num_negatives += 1

        return total_num_negatives



class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        """
        Count the negatives from the bottom right to the bottom left,
        then right to left sequentially for each row increasing from
        the bottom.

        In order to maximize efficiency, the search will never go past
        the maximum number of negative numbers on the previous line.
        This is possible because we know that ordering is non-decreasing
        both row wise and column wise.
        """

        total_num_negatives = 0

        num_to_search = len(grid[0])

        for i, row in enumerate(reversed(grid)):
            num_neg_in_row = 0
            for j in range(num_to_search):
                element = row[-j-1]
                if element < 0:
                    num_neg_in_row += 1

            num_to_search = num_neg_in_row
            total_num_negatives += num_neg_in_row

        return total_num_negatives