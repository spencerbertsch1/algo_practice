"""
1304. Find N Unique Integers Sum up to Zero

Given an integer n, return any array containing n unique integers such that they add up to 0.
"""
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        """
        Retruns a list of ints which sum to zero
        """
        # add the edge case where n=1
        half_n: int = round((n * 0.5) - 0.1)  # <-- make sure we round down
        sum_list = []

        # edge case when n is 1
        if (n == 1):
            sum_list: list = [0]

        # if n is odd
        elif (n%2 != 0):
            sum_list: list = [0]
            for i in range(half_n):
                i_to_add = i+1
                sum_list.append(-i_to_add)
                sum_list.append(i_to_add)

        # if n is even
        elif (n%2 == 0):
            sum_list: list = []
            for i in range(half_n):
                i_to_add = i+1
                sum_list.append(-i_to_add)
                sum_list.append(i_to_add)

        return sum_list


if __name__ == "__main__":
    s = Solution()
    print(s.sumZero(n=5))
