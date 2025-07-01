
def slice_me(family: list, start: int, end: int) -> list:
    '''
    takes as parameters a 2D array, prints its shape,
    return: a truncated version of the array based on start and end
    '''
    if not isinstance(family, list):
        raise ValueError("non list argument")
    if not family or not all(isinstance(row, list) for row in family):
        raise ValueError("Input array is not 2D or is empty")

    try:
        f_row_len = len(family[0])
        if not all(len(row) == f_row_len for row in family):

if __name__ == "__main__":

    family = [[1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))