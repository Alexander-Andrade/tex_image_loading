import scipy
import scipy.ndimage
import timeit
from PIL import Image
import numpy as np
from scipy.misc import toimage

if __name__=="__main__":
    print("scipy ndimage")
    start = timeit.timeit()
    simage = scipy.ndimage.imread("hd.jpg")
    #print(simage)
    width, height, bytes_per_pix = simage.shape
    image = np.reshape(simage, (width * height, bytes_per_pix))
    end = timeit.timeit()
    print(end-start)
    print(image)
    # toimage(simage).show()

    #print(image.data)

    print("pillow")
    start = timeit.timeit()
    img = Image.open("hd.jpg")
    #toimage(img).show()
    #print(np.array(img))
    pimgage = np.array(list(img.getdata()), np.uint8)
    end = timeit.timeit()
    print(end - start)
    print(pimgage)

    if np.array_equal(image, pimgage):
        print("ravny")


