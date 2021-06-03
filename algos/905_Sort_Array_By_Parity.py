class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens: list = []
        odds: list = []
        for num in nums: 
            if num%2==0:
                evens.append(num)
            else:
                odds.append(num)
                
        return evens+odds
