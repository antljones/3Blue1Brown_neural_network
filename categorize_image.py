#/usr/bin/python3

import numpy as np
import idx2numpy
import matplotlib.pyplot as plt

imagefile= './training_data/train-images-idx3-ubyte'
imagearray = idx2numpy.convert_from_file(image_file)

plt.imshow(imagearray[4], cmap=plt.cm.binary)
