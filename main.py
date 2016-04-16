from Algorithm import Diffuse, functions
from skimage import io
import matplotlib.pyplot as plt


diffuse = Diffuse.Diffuse(functions.h1)

image = io.imread('Images/frutas.jpg')
diffuse_image = diffuse.apply('Images/frutas.jpg', 0.5, 20, 40)

fig, (img, dif) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

img.imshow(image)
dif.imshow(diffuse_image)

fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0.02, left=0.02, right=0.98)

plt.show()