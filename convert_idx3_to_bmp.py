import struct
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# filename = "../../data/mnist/train-images-idx3-ubyte"
filename = "training_data/train-images-idx3-ubyte"

binfile = open(filename, 'rb')
buf = binfile.read()

index = 0
# read 4 unsigned int with big-endian format
magic, numImages, numRows, numColumns = struct.unpack_from('>IIII', buf, index)
index += struct.calcsize('>IIII') # move the cursor

for image in range(0, numImages):
    # the image is 28*28=784 unsigned chars
    im = struct.unpack_from('>784B', buf, index)
    index += struct.calcsize('>784B') # move the cursor
   
    # create a np array to save the image
    im = np.array(im, dtype='uint8')
    im = im.reshape(28, 28)
    
    # # display the image
    # plt.imshow(im, cmap='gray')
    # plt.show()
    
    im = Image.fromarray(im)
    im.save("training_data/train_%s.bmp" % image, "bmp")
