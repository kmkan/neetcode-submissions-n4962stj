import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict_tasks = defaultdict(int)

        for t in tasks: 
            dict_tasks[t] += 1
        
        new_tasks = []

        for k, v in dict_tasks.items():
            new_tasks.append((v * -1, k))
        
        heapq.heapify(new_tasks)
        print(new_tasks)
        total_cycles = 0
        while new_tasks:
            cur_cycles = 0
            cur_tasks = []

            while new_tasks:
                val, task = heapq.heappop(new_tasks)
                val += 1
                if val < 0:
                    cur_tasks.append((val, task))
                cur_cycles += 1
                if cur_cycles >= n + 1:
                    break
            for t in cur_tasks:
                heapq.heappush(new_tasks, t)
            if new_tasks and cur_cycles < n + 1:
                total_cycles += n + 1
            else:
                total_cycles += cur_cycles
            print(new_tasks, total_cycles)
        return total_cycles
