class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        return self.move(abs(x), abs(y), {})

    def move(self, x: int, y: int, previousCounts: dict) -> int:
        if x + y == 0:
            return 0
        if x + y == 2:
            return 2
        if (x, y) in previousCounts:
            return previousCounts[(x, y)]

        res = min(self.move(abs(x - 1), abs(y - 2), previousCounts),
                  self.move(abs(x - 2), abs(y - 1), previousCounts)) + 1

        previousCounts[(x, y)] = res
        return res