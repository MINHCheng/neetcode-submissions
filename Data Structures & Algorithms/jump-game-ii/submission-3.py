class Solution:
    def jump(self, nums: List[int]) -> int:
        visited = {0}
        if not nums or len(nums)==1:
            return 0
        queue = collections.deque([0])
        jumps = 0
        while queue:
            jumps+=1
            for _ in range(len(queue)):
                val = queue.popleft()
                for v in range(1, nums[val] + 1):
                    search = v + val
                    if search >= len(nums)-1:
                        return jumps
                    if search not in visited:
                        visited.add(search)
                        queue.append(search)
        return 0