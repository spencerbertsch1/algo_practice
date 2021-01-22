"""
1051. Height Checker

Students are asked to stand in non-decreasing order of
heights for an annual photo.

Return the minimum number of students that must move in
order for all students to be standing in non-decreasing
order of height.

Notice that when a group of students is selected they can
reorder in any possible way between themselves and the non
selected students remain on their seats.
"""
from typing import List


class Solution:

    def heightChecker(self, heights: List[int]) -> int:
        # We only need to retuen the number of students that need to be moved
        sorted_heights = heights.copy()  # <-- we need to make a copy so we create a new place in memory
        sorted_heights.sort()

        solution = 0
        for height, sorted_height in zip(heights, sorted_heights):
            if height != sorted_height:
                solution += 1

        return solution
