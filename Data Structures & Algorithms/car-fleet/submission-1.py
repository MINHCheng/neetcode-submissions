import heapq

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        groups = []
        for i, p in enumerate(position):  # Fixed variable name (position)
            heapq.heappush(groups, (-p, i))

        res = 0
        prev_time = 0  # Track the time of the fleet ahead
        
        while groups:
            neg_p, i = heapq.heappop(groups)  # Fixed unpacking syntax
            p = -neg_p                        # Recover original position
            
            # Use regular float division (/), not integer division (//)
            t = (target - p) / speed[i]
            
            # If the current car takes MORE time than the fleet ahead of it,
            # it cannot catch them and must form a new fleet.
            if t > prev_time:
                res += 1
                prev_time = t  # Update the bottleneck time for cars further back
                
        return res