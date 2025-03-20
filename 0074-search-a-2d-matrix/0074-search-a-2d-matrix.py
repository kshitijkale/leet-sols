class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            m = len(matrix)  # no of rows
            n = len(matrix[0]) # NO OF COLUMNS 
            

            l = 0
            h = m-1

            while(l<=h):
                c = l + (h-l)//2
                if matrix[c][0] == target:
                    return True
                elif matrix[c][0] < target:
                    if c == m-1 or matrix[c+1][0] > target:
                        # binary search in row c
                        row = matrix[c]
                        left, right = 0, n - 1
                        while left <= right:
                            mid2 = left + (right - left) // 2
                            if row[mid2] == target:
                                return True
                            elif row[mid2] < target:
                                left = mid2 + 1
                            else:
                                right = mid2 - 1
                        return False  # Target not found in row
                    else:
                        l = c+1
                else:
                        h = c-1

            return False


        