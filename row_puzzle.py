# Author: Rajvi Rajput
# GitHub username: rrajput22
# Date: 11/08/2023
# Description: Recursive function named row_puzzle that takes a list of integers (the row) as a parameter
# and returns True if the puzzle is solvable for that row, but returns False otherwise.
# After the function has finished, the list is the same as it was when the function was called.


def row_puzzle(row, current_index=0, visited_set=None):
    """
    Recursive function to check if the row puzzle is solvable.
    """
    # Initializes visited set if not provided, memoization so that the function does not revisit the same index
    if visited_set is None:
        visited_set = set()

    # Base case: If the token reaches the rightmost square
    # as long as the token reaches the rightmost square, zeros in other squares are allowed
    if current_index == len(row) - 1:
        return True

    # Check if the current index is already visited
    if current_index in visited_set:
        return False

    # Adds the current index to visited set
    visited_set.add(current_index)

    # Moves right or left based on the value in the current square
    move_right = current_index + row[current_index]
    move_left = current_index - row[current_index]

    # Recursive calls for both directions
    if 0 <= move_right < len(row) and row_puzzle(row, move_right, visited_set):
        return True
    if 0 <= move_left < len(row) and row_puzzle(row, move_left, visited_set):
        return True

    # If neither direction leads to a solution, return False
    return False
