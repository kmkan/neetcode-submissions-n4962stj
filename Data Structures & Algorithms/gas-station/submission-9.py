class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        sum_total = 0
        idx = -1
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            sum_total += gas[i] - cost[i]
            print(total)
            if total < 0:
                total = 0
                idx = -1
            elif total >= 0 and total - gas[i] + cost[i] <= 0:
                idx = i
        
        if sum_total < 0:
            return -1
        return idx
