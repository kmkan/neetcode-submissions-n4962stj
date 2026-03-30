class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net = [gas[i] - cost[i] for i in range(len(gas))]

        if sum(net) < 0:
            return -1
        

        total = 0
        idx = -1


        print(net)
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            print(total)
            if total < 0:
                total = 0
                idx = -1
            elif total >= 0 and total - gas[i] + cost[i] <= 0:
                idx = i
        
        return idx
