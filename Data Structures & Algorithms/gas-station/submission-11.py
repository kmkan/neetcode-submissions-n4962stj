class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        sum_total = 0
        idx = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            sum_total += gas[i] - cost[i]


            if total < 0:
                total = 0
                idx = i + 1
        
        if sum_total < 0:
            return -1
        return idx
