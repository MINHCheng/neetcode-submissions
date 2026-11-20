class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-float('inf'))
        maxHeap = []
        result = 0
        for i, h in enumerate(heights):
            height, index = h,i
            while maxHeap:
                if -maxHeap[0][0] > h:
                    height, popped_index = maxHeap[0]
                    index = min(index, popped_index)
                    result = max(-height * (i - index), result)
                    heapq.heappop(maxHeap)
                else:
                    break
            heapq.heappush(maxHeap, (-h, index))
            
            result = max(height * (i - index), result)

        return result
                    
        