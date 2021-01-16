"""
217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        if (len(set(nums)) != len(nums)):
            solution=True
        else:
            solution=False

        return solution

# let's look at a cleaner solution:

class BetterSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return (len(nums) != len(set(nums)))