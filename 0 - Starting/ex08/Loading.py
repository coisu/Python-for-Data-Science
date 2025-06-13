def ft_tqdm(lst: range) -> None:
    try:
        total = len(lst)
    except TypeError:
        print("Error: Not a valid iterable object for ft_tqdm")
        return
    bar_max = 87
    for i, item in enumerate(lst):
        yield item

        progress = (i + 1) / total
        cur = int(bar_max * progress)
        bar = '█' * cur + ' ' * (bar_max - cur)
        print(f"{int(progress * 100):>3}%|{bar}| {i + 1}/{total}", end='\r', flush=True)
    
# if __name__ == "__main__":
#     from time import sleep
#     from tqdm import tqdm
#     for elem in ft_tqdm(range(333)):
#         sleep(0.005)
#     print()
#     for elem in tqdm(range(333)):
#         sleep(0.005)
#     print()