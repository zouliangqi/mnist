from tensorflow.examples.tutorials.mnist import input_data
import os
import scipy.misc

mnist =input_data.read_data_sets("MNIST_data",one_hot=True)

sava_dir='MNIST_data/raw'
if os.path.exists(sava_dir) is False:
	os.makedirs(sava_dir)

for i in range(10):
	image_array=mnist.train.images[i,:]
	image_array=image_array.reshape(28,28)
	filename=sava_dir+'mnist_train_%d.jpg'%i
	scipy.misc.toimage(image_array,cmin=0.0,cmax=1.0).save(filename)