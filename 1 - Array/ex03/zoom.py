from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def print_pxl(pxl: np.ndarray):
    try:
        plt.imshow(pxl, cmap='gray')
        plt.show()
    except Exception as e:
        print(f"Unexpected error occurred in print_pxl: {e}")


def ft_zoom(pxl: np.ndarray):
    try:
        color = Image.fromarray(pxl)
        gray = np.array(color.convert('L'))  # 8-bit grayscale

        h, w = gray.shape
        zoom_size = 400

        center_x = w // 2
        center_y = h // 2
        x = center_x - (zoom_size // 2)
        y = center_y - (zoom_size // 2)
        zoomed = gray[y: y + zoom_size, x: x + zoom_size]

        expanded_dims = np.expand_dims(zoomed, axis=2)
        print(f"New shape after slicing: \
{expanded_dims.shape} or {zoomed.shape}")

        return zoomed, expanded_dims

    except Exception as e:
        print(f"Unexpected error occurred in ft_zoom: {e}")


if __name__ == "__main__":
    pxl = ft_load("animal.jpeg")
    if pxl is not None:
        print(pxl)
        zoomed, shaped = ft_zoom(pxl)
        if zoomed is not None:
            print(shaped)
            print_pxl(zoomed)

'''
The shape of image is: (768, 1024, 3)
[[[120 111 132]
[139 130 151]
[155 146 167]
...
[120 156 94]
[119 154 90]
[118 153 89]]]
New shape after slicing: (400, 400, 1) or (400, 400)
[[[167]
[180]
[194]
...
[102]
[104]
[103]]]
'''
