class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net = [gas[i] - cost[i] for i in range(len(gas))]

        if sum(net) < 0:
            return -1
        

        total = 0
        max_total = float('-inf')
        idx = -1


        print(net)
        for i in range(len(net)):
            total += net[i]
            print(total)
            if total < 0:
                total = 0
                idx = -1
            elif total >= 0 and total - net[i] <= 0:
                idx = i
        
        return idx
