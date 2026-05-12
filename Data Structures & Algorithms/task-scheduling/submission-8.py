class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict_heap = {}

        for t in tasks:
            dict_heap[t] = dict_heap.get(t, 0) + 1
        
        heap = [(-count, letter) for letter, count in dict_heap.items()]

        heapq.heapify(heap)

        total_cycles = 0

        while heap:
            cur_cycles = 0
            extracted = []
            while heap and cur_cycles < n + 1:
                count, letter = heapq.heappop(heap)
                count *= -1
                count -= 1
                if count > 0:
                    extracted.append((-count, letter))
                cur_cycles += 1
            print(f'Extracted: {extracted}, Current Cycles: {cur_cycles}')
            if not extracted or cur_cycles == n + 1:
                total_cycles += cur_cycles
            else:
                total_cycles += n + 1
            for c in extracted:
                heapq.heappush(heap, c)
            print(f'Total cycles: {total_cycles}')
        return total_cycles
