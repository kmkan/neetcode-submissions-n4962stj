from collections import defaultdict
import heapq
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dict = defaultdict(int)

        for t in tasks:
            task_dict[t] += 1
        

        task_arr = []
        for k, v in task_dict.items():
            task_arr.append((v, k))

        task_arr.sort(reverse=True)

        total_cycles = 0

        while task_arr:
            cur_cycles = 0
            i = 0
            while i < len(task_arr):
                task_count, task = task_arr[i]
                task_arr[i] = (task_count - 1, task)
                cur_cycles += 1
                if task_count - 1 == 0:
                    task_arr.remove((task_count - 1, task))
                else:
                    i += 1
                if cur_cycles == n + 1:
                    break
            if task_arr and cur_cycles < n + 1:
                total_cycles += n + 1
            else:
                total_cycles += cur_cycles
            task_arr.sort(reverse=True)
            print(task_arr, total_cycles)
            

        return total_cycles