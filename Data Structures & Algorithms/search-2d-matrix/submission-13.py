class Solution:
    def bs(self, val, target):
        if (len(val) == 1):
            return val[0] == target
        left = 0
        right = len(val) - 1
        while left <= right:
            mid = (left + right) // 2
            if val[mid] == target:
                return True
            elif val[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if (len(matrix) == 1):
            return self.bs(matrix[0], target)
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][-1] >= target and matrix[mid][0] <= target:
                return self.bs(matrix[mid], target)
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False