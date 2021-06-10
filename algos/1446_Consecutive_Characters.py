class Solution:
    def maxPower(self, s: str) -> int:
        max_num = 1
        counter = 1
        for i in range(1, len(s)): 
            if(s[i-1] == s[i]):
                counter+=1
            else: 
                counter=1
            max_num = max(counter, max_num)
        return max_num
