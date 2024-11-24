import math
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        lowest_absolute_number = 200000 # greater than 100000
        even_number_of_negatives = True
        total_absolute_count = 0
        matrix_contains_zero = True

        for row in matrix:
            for cell in row:
                if cell == 0:
                    matrix_contains_zero = False
                    lowest_absolute_number = 0
                    continue
                elif cell < 0:
                    cell = -cell
                    even_number_of_negatives = not even_number_of_negatives
                if matrix_contains_zero:
                    lowest_absolute_number = min(cell, lowest_absolute_number)
                total_absolute_count += cell
                
        if not even_number_of_negatives:
            total_absolute_count -= lowest_absolute_number*2

        return total_absolute_count
