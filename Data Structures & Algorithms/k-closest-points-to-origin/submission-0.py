class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points :
            distance = ((x)**2 + (y)**2)
            topVal = -maxHeap[0][0] if maxHeap else None
            
            if len(maxHeap) >= k:
                if distance < topVal:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, (-distance, [x,y]))
            else:
                heapq.heappush(maxHeap, (-distance, [x,y]))
        return [h[1] for h in maxHeap]