#/bin/bash

sudo yum -y install python3-devel libjpeg libjpeg-devel zlib libtiff freetype freetype-devel libwebp tcl/tk openjpeg libimagequant libraqm

python3 -m pip install Pillow
python3 -m pip install numpy
python3 -m pip install idx2numpy
python3 -m pip install matplotlib

MNIST_TRAINING_FILE=./training_data/train-images-idx3-ubyte
if [ -d "$FILE" ]; then
    echo "$FILE already exists..skipping"]
else
    cd ./training_data/
    wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
    gzip -d train-images-idx3-ubyte.gz
    cd ..
fi


