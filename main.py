import scipy
import scipy.ndimage
import timeit
from PIL import Image
import numpy as np
import scipy.ndimage.interpolation
from scipy.misc import toimage

if __name__=="__main__":
    print("scipy ndimage")
    start = timeit.timeit()

    sci_image = scipy.ndimage.imread("hd.jpg")
    sci_image = np.fliplr(sci_image)
    sci_image = scipy.ndimage.interpolation.rotate(sci_image, 180)

    width, height, bytes_per_pix = sci_image.shape
    sci_image = np.reshape(sci_image, (width * height, bytes_per_pix))

    end = timeit.timeit()
    print(end-start)

    # toimage(simage).show()

    print("pillow")
    start = timeit.timeit()

    pil_image = Image.open("hd.jpg")
    pil_image = pil_image.transpose(Image.FLIP_LEFT_RIGHT).rotate(180)

    #toimage(img).show()
    #print(np.array(img))

    pil_image = np.array(list(pil_image.getdata()), np.uint8)

    end = timeit.timeit()
    print(end - start)
    print(pil_image)

    print(sci_image[width * height-6])
    print(pil_image[width * height-6])

    for i in range(sci_image.shape[0]):
        if not (sci_image[i] == pil_image[i]).all():
            print(i)

    if np.array_equal(image, pimgage):
        print("ravny")


