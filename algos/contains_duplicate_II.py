"""
219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the
array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Given an array of integers and an integer k, find out whether there are two distinct
        indices i and j in the array such that nums[i] = nums[j] and the absolute difference
        between i and j is at most k.
        :arg: nums - list, list of input integers
        :arg: k - int, integer representing the abs(diff) between values in nums

        """
        solution: bool = False

        # iterate through the list remembering the outer index
        for outer_index, i in enumerate(nums):
            # iterate through what's left of the list starting at the outer index
            for inner_index, j in enumerate(nums[(outer_index+1):]):
                # if list[i] is equal to list[j]
                if (i == j):
                    # and if the total indices are less than k
                    if (abs(outer_index-(outer_index+inner_index))  < k):
                        solution: bool = True

        return solution

# This solution works, but sadly it takes a long time. Lets look at a better solution:
class OtherSolution:
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        # iterate through all of the values in the list (i=index, v=value)
        for i, v in enumerate(nums):
            # if the value already resides in the keys in the dictionary...
            if (v in dic):
                # and if the difference between the current index and the other index is less than k...
                if (i - dic[v] <= k):
                    return True
            dic[v] = i
        return False

