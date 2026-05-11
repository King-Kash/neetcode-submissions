class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1
        
        max_heap = []

        for val in counts.values():
            heapq.heappush(max_heap, val*-1)

        queue = []
        timer = 0
        while queue or max_heap:
            timer += 1

            if max_heap:
                top_val = heapq.heappop(max_heap) * -1
                top_val -= 1
                print(top_val)
                if top_val > 0:
                    queue.append((top_val, timer + n))
            
            if queue:
                oldest = queue[0]
                if timer >= oldest[1]:
                    reinsert = queue.pop(0)
                    heapq.heappush(max_heap, reinsert[0] * -1)
            
        return timer



