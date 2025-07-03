
def slice_me(family: list, start: int, end: int) -> list:
    '''
    Takes a 2D list, prints its shape, and returns a truncated version.
    slicing
    Args:
        family (list): A 2D list (list of lists).
        start (int): The starting index for the slice.
        end (int): The ending index for the slice.

    shape(row, col)
    start-end: row num
    slicing (0, 2): row index 0 to 1 (exclude 2)
    negative indexing (-1, -2 ...): row index from backward

    Returns:
        list: The truncated 2D list.
    '''

    if not isinstance(family, list) or \
            not all(isinstance(row, list) for row in family):
        raise ValueError("Error: Wrong input type: must be a 2D list")
    if not family:
        shape = (0, 0)
    else:
        row_size = len(family[0])
        if not all(len(row) == row_size for row in family):
            raise ValueError("Error: All inner lists must have the same size.")
        shape = (len(family), row_size)

    print(f"My shape is : {shape}")
    new_family = family[start:end]
    if not new_family:
        new_shape = (0, 0)
    else:
        new_shape = (len(new_family), len(new_family[0]))
    print(f"My new shape is : {new_shape}")
    return new_family

# if __name__ == "__main__":

#     family = [[1.80, 78.4], # 0 / -4
#             [2.15, 102.7],  # 1 / -3
#             [2.10, 98.5],   # 2 / -2
#             [1.88, 75.2]]   # 3 / -1
#     print(slice_me(family, 0, 2))
#     print(slice_me(family, 1, -2))
#     print(slice_me(family, -3, 3))
