def NULL_not_found(object: any) -> int:
    try:
        if object is None:
            print(f"{object}: {type(object)}")
        # if isinstance(object, str):
        #     print(f"{object} is in the kitchen : {type(object)}")
        # elif isinstance(object, list):
        #     print(f"List : {type(object)}")
        # elif isinstance(object, tuple):
        #     print(f"Tuple : {type(object)}")
        # elif isinstance(object, set):
        #     print(f"Set : {type(object)}")
        # elif isinstance(object, dict):
        #     print(f"Dict : {type(object)}")
        # else:
        #     print("Type not found")
    
    return 1

if __name__ == "__main__":
    from NULL_not_found import NULL_not_found
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ''
    Fake = False
    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    print(NULL_not_found("Brian"))