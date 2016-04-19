from Algorithm import Diffuse, functions
from skimage import io
import matplotlib.pyplot as plt
import datetime
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'


images_path = functions.images_path()
lambda_1 = 0.25
k = 20;
i = 10
diffuse_1 = Diffuse.Diffuse(functions.h1)
diffuse_2 = Diffuse.Diffuse(functions.h2)


def test_k():
    counter = 0
    for image_path in images_path:
        print "Working with " + image_path+" at "+str(datetime.datetime.now())
        image = io.imread(image_path)
        print "h 1 at "+str(datetime.datetime.now())
        diffuse1 = diffuse_1.apply(image_path, lambda_1, k, i)
        print "h 2 at "+str(datetime.datetime.now())
        diffuse2 = diffuse_2.apply(image_path, lambda_1, k, i)
        print "Saving"
        fig, (img, dif1, dif2) = plt.subplots(nrows=1, ncols=3, figsize=(10, 5))

        img.imshow(image, cmap=plt.cm.gray)
        dif1.imshow(diffuse1, cmap=plt.cm.gray)
        dif2.imshow(diffuse2, cmap=plt.cm.gray)

        fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0.02, left=0.02, right=0.98)

        plt.savefig('Images/h_test/Example'+str(counter)+'.png', bbox_inches='tight')
        counter += 1