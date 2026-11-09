class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        
        hashmap = {}
        for c in hand:
            hashmap[c] = hashmap.get(c, 0) + 1
            
        minH = list(hashmap)
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in hashmap:
                    return False
                hashmap[i]-=1
                if hashmap[i] == 0:
                    if i is not minH[0]:
                        return False
                    heapq.heappop(minH)
        return True