class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1
        
        max_heap = []
        for key in counts.keys():
            alpha_count = counts[key] * -1
            heapq.heappush(max_heap, alpha_count)
        
        queue = []
        timer = 0
        while queue or max_heap:
            timer += 1
            
            if max_heap:
                top_count = heapq.heappop(max_heap) * -1 
                # gives us count of unprocessed letter with highest frequency at the present
                new_count = top_count - 1
                if new_count > 0: 
                    queue.append((new_count, timer + n))
            
            if queue:
                if timer >= queue[0][1]:
                    reinsert = queue.pop(0)
                    heapq.heappush(max_heap, reinsert[0]*-1)
        
        return timer


        