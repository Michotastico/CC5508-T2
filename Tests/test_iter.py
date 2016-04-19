from Algorithm import Diffuse, functions
from skimage import io
import matplotlib.pyplot as plt
import datetime
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'


images_path = functions.images_path()
lambda_1 = 0.25
k = 20
i_1 = 5;
i_2 = 10;
i_3 = 15;

i = 20
diffuse = Diffuse.Diffuse(functions.h1)


def test_iter():
    counter = 0
    for image_path in images_path:
        print "Working with " + image_path+" at "+str(datetime.datetime.now())
        image = io.imread(image_path)
        print "Iter 1 at "+str(datetime.datetime.now())
        diffuse1 = diffuse.apply(image_path, lambda_1, k, i_1)
        print "Iter 2 at "+str(datetime.datetime.now())
        diffuse2 = diffuse.apply(image_path, lambda_1, k, i_2)
        print "Iter 3 at "+str(datetime.datetime.now())
        diffuse3 = diffuse.apply(image_path, lambda_1, k, i_3)
        print "Saving"
        fig, ((img, dif1), (dif2, dif3)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))

        img.imshow(image, cmap=plt.cm.gray)
        dif1.imshow(diffuse1, cmap=plt.cm.gray)
        dif2.imshow(diffuse2, cmap=plt.cm.gray)
        dif3.imshow(diffuse3, cmap=plt.cm.gray)

        fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0.02, left=0.02, right=0.98)

        plt.savefig('Images/iter_test/Example'+str(counter)+'.png', bbox_inches='tight')
        counter += 1