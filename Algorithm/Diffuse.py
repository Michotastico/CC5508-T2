import numpy
from skimage import io
import functions


class Diffuse:
    def __init__(self, h):
        self.h = h

    def apply(self, image_path, lamb, k, iterations):
        image = io.imread(image_path)
        original_type = image.dtype
        image = image.astype(numpy.float16)

        size = image.shape
        width = size[0]
        height = size[1]

        for i in range(0, iterations):
            img = image.copy()

            for x in range(0, width):
                for y in range(0, height):
                    top = 0
                    down = 0
                    left = 0
                    right = 0
                    if x > 0:
                        left = img[x - 1, y]
                    if x < (width - 1):
                        right = img[x + 1, y]
                    if y > 0:
                        down = img[x, y - 1]
                    if y < (height - 1):
                        top = img[x, y + 1]
                    center = img[x, y]
                    new_center = functions.diffuse(self.h, k, lamb, top, down, center, left, right)
                    image[x, y] = new_center

        return_image = image.copy()
        return_image = return_image.astype(original_type)
        return return_image



