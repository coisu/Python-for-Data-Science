
def all_thing_is_obj(object: any) -> int:
    if isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
    elif isinstance(object, list):
        print(f"List : {type(object)}")
    elif isinstance(object, tuple):
        print(f"Tuple : {type(object)}")
    elif isinstance(object, set):
        print(f"Set : {type(object)}")
    elif isinstance(object, dict):
        print(f"Dict : {type(object)}")
    else:
        print("Type not found")
    return 42

# if __name__ == "__main__":
#     from find_ft_type import all_thing_is_obj
#     ft_list = ["Hello", "tata!"]
#     ft_tuple = ("Hello", "toto!")
#     ft_set = {"Hello", "tutu!"}
#     ft_dict = {"Hello" : "titi!"}
#     all_thing_is_obj(ft_list)
#     all_thing_is_obj(ft_tuple)
#     all_thing_is_obj(ft_set)
#     all_thing_is_obj(ft_dict)
#     all_thing_is_obj("Brian")
#     all_thing_is_obj("Toto")
#     print(all_thing_is_obj(10))