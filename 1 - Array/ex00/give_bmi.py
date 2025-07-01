def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    '''
    take 2 lists of integers or floats in input and returns a list
    of BMI values.
    '''
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same size.")
    lst = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise ValueError("height and weight must be integers or floats.")
        if h <= 0 or w <= 0:
            raise ValueError("Height and weight must be positive values.")
        
        lst.append(w / (h ** 2))

    return lst

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    accepts a list of integers or floats and an integer representing
    a limit as parameters. It returns a list of booleans
    (True if above the limit).
    '''
    # np_bmi = np.array(bmi)
    # result_array = np_bmi > limit
    # return result_array.tolist()
    return [val > limit for val in bmi]

# if __name__ == "__main__":
#     # from give_bmi import give_bmi, apply_limit
#     height = [2.71, 1.15]
#     weight = [165.3, 38.4]
#     bmi = give_bmi(height, weight)
#     print(bmi, type(bmi))
#     print(apply_limit(bmi, 26))