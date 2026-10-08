class CountSquares:

    def __init__(self):
        self.point_list = {}

    def add(self, point: List[int]) -> None:
        c = tuple(point)
        self.point_list[c] = self.point_list.get(c, 0) + 1

    def count(self, point: List[int]) -> int:
        res = 0
        point = tuple(point)
        for p in self.point_list:
            left = tuple((p[0], point[1]))
            right = tuple((point[0], p[1]))

            count = 0
            if p[0] != point[0] and p[1] != point[1]:
                if left in self.point_list and right in self.point_list:
                    count = self.point_list[p]
                    count *= self.point_list[left]
                    count *= self.point_list[right]
            res += count

        return res

        
