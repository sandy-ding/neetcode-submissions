class CountSquares:

    def __init__(self):
        self.map_ = defaultdict(int)
        self.arr = []     

    def add(self, point: List[int]) -> None:
        self.map_[tuple(point)] += 1
        self.arr.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.arr:
            if abs(x - px) != abs(y - py) or (x == px and y == py):
                continue
            res += self.map_[(x, py)] * self.map_[(px, y)]

        return res
                        



        
