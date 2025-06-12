def NULL_not_found(object: any) -> int:

    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} {type(object)}")
        return 0
    elif isinstance(object, bool) and object == False:
        print(f"Fake: {object} {type(object)}")
        return 0
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif isinstance(object, str) and object == '':
        print(f"Empty: {object} {type(object)}")
        return 0
    else:
        print("Type not found")
    
    return 1

# if __name__ == "__main__":
#     from NULL_not_found import NULL_not_found
#     Nothing = None
#     Garlic = float("NaN")
#     Zero = 0
#     Empty = ''
#     Fake = False
#     NULL_not_found(Nothing)
#     NULL_not_found(Garlic)
#     NULL_not_found(Zero)
#     NULL_not_found(Empty)
#     NULL_not_found(Fake)
#     print(NULL_not_found("Brian"))