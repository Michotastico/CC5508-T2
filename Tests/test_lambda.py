from Algorithm import Diffuse, functions
from skimage import io
import matplotlib.pyplot as plt
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'


images_path = functions.images_path()
lambda_1 = 0.10
lambda_2 = 0.25
k = 20
i = 20
diffuse = Diffuse.Diffuse(functions.h1)


def test_lambda():
    counter = 0
    for image_path in images_path:
        image = io.imread(image_path)
        diffuse1 = diffuse.apply(image_path, lambda_1, k, i)
        diffuse2 = diffuse.apply(image_path, lambda_2, k, i)

        fig, (img, dif1, dif2) = plt.subplots(nrows=1, ncols=3, figsize=(10, 5))

        img.imshow(image, cmap=plt.cm.gray)
        dif1.imshow(diffuse1, cmap=plt.cm.gray)
        dif2.imshow(diffuse2, cmap=plt.cm.gray)

        fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0.02, left=0.02, right=0.98)

        plt.savefig('Images/lambda_test/Example'+str(counter)+'.png', bbox_inches='tight')
        counter += 1
