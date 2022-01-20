class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in matrix:
            if set(i) != set(range(1, n + 1)):
                return False
        for i in zip(*matrix):
            if set(i) != set(range(1, n + 1)):
                return False
        return True
