from PIL import Image
import numpy as np
import os


def ft_load(path: str):
    '''
    loads an image
    need to JPG and JPEG format.

    Args:
        path (str): The file path to the image.

    Pint: its format, and its pixels content in RGB format.
        [[r, g, b]]

    Sape: (height, width, number of color channel)

    color channel:
        1 = grayscale(0-255), 3 = rgb, 4 = (rgba(opacity) or CMYK)
    '''
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Error: The file {path} not found.")
        img = Image.open(path)
        print(f"Image fornat: {img.format}")
        if img.format != 'JPEG' and img.format != 'JPG':
            raise TypeError("Error: Only JPG and JPEG fornats are supported.")
        # width, height = img.size
        # channels = len(img.getbands())
        # print(f"The shape of image is: ({height}, {width}, {channels})")
        pxl = np.array(img)
        print(f"The shape of image is: {pxl.shape}")

        return pxl
    except (FileNotFoundError, TypeError) as e:
        print(e)
        return None
    except Exception as e:
        print(f"unexpected error occured: {e}")
        return None


'''
pxl.shape: (height, width, number of color channel)
pxl.ndim: number of dimensions in array
pxl.size: row * col * channel
pxl.dtype: data type -> uint8(0 - 255)
pxl.copy(), pxl.mean(), pxl.min(), pxl.max()
pxl[y, x]: access to a certain pixel,
    print(pxl[100, 50]) >> [138  89  64]
    pxl[100, 50, 2]: row 100,  col 50, RGB b
    pxl[:,  :, 0]: among total row, total col, select RGB r values > 2D array
pxl[y1:y2, x1:x2]: trim square area of image
'''

# if __name__ == "__main__":
#     print(ft_load("landscape.jpg"))

# The shape of image is: (257, 450, 3)
# [[[19 42 83]
# [23 42 84]
# [28 43 84]
# ...
# [ 0 0 0]
# [ 1 1 1]
# [ 1 1 1]]]

# [
#     [ # row 0:
#         [19, 42, 83],
#         [23, 42, 84],
#         ... # (450 rgb pixels in total
#     ],
#     [ # row 1:
#         ... # (450 rgb pixels in total
#     ],
#     ... # (row  - 256)
# ]
