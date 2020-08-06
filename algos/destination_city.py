"""
1436. Destination City

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. 
Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
"""
from typing import List 

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # create the initial destinations list 
        destinations = []
        for path in paths:
            destinations.append(path[-1])
                
        # clean out the destinations list 
        for path in paths:
            for location in range(len(path)-1):
                if path[location] in destinations:
                    destinations.remove(path[location])
                
        return destinations[0]


class BetterSolution:
        def destCity(self, paths: List[List[str]]) -> str:
            """
            :type paths: List[List[str]]
            :rtype: str
            """
            # create dictionary if possible (only when k-v are both present)
            dic = {p[0]:p[1] for p in paths}
            A = paths[0][0]
            while True:
                try:
                    A = dic[A]
                except:
                    return A