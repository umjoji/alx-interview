#!/usr/bin/python3
'''0x09. Island Perimeter'''

from typing import List

def is_water(grid: List[List[int]], row: int, col: int) -> bool:
    '''
    Checks if a cell is water (0) or out of bounds.

    Args:
        grid (List[List[int]]): The grid representing the island.
        row (int): The row index of the cell.
        col (int): The column index of the cell.

    Returns:
        bool: True if the cell is water or out of bounds, False otherwise.
    '''
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
        return True
    return False

def count_perimeter(grid: List[List[int]]) -> int:
    '''
    Counts the perimeter of the island described in the grid.

    Args:
        grid (List[List[int]]): The grid representing the island.

    Returns:
        int: The total perimeter of the island.
    '''
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                # Check adjacent cells and increment the perimeter
                if is_water(grid, row - 1, col):
                    perimeter += 1
                if is_water(grid, row + 1, col):
                    perimeter += 1
                if is_water(grid, row, col - 1):
                    perimeter += 1
                if is_water(grid, row, col + 1):
                    perimeter += 1

    return perimeter

def island_perimeter(grid: List[List[int]]) -> int:
    '''
    Returns the perimeter of the island described in grid.

    Args:
        grid (List[List[int]]): The grid representing the island.

    Returns:
        int: The total perimeter of the island.
    '''
    return count_perimeter(grid)
