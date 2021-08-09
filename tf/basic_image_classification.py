# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

#print(tf.__version__)

fashion_mnist = tf.keras.datasets.fashion_mnist

"""Training images+labels are the raw unclassified data, testing are for comparison"""
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# return: number of images, pixel_width, pixel_height - ex. (60000, 28, 28)
#print(train_images.shape)

#print(len(train_labels)) # 60,000 as well
#print(train_labels) # each label is an int index, ie 9, 0, 0, 3, 0, 5 representing correct label from class_names

"""Here we preprocess the data, this example is just the first image."""
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
#plt.show()

"""Each pixel holds a value from 0 to 255, which we must reduce to a scale of 0 to 1."""
train_images = train_images / 255.0
test_images = test_images / 255.0

"""Display the first 25 images to verify preprocessing."""
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
#plt.show()

"""Set up our model with several layers in it.
Flatten converts each 28x28 2D array into a 784px 1D array.
First Dense has 128 'nodes' or 'neurons'.
Second Dense returns a logits array of length 10, 
each node holding a score indicating the image belongs to that class.
"""
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

"""Compile the model.
Loss function -- accuracy, minimize it for higher accuracy.
Optimizer -- how the model is updated based on loss function and new data.
Metrics -- how to gauge success, in this case how many images correctly classified
"""
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

"""Actual training here.
1. Feed the training data to the model.
2. Model learns to associate images with labels.
3. Model makes predictions about test set (known).
4. Compare predictions against test_labels array.

So step 1 data is first argument, step 4 uses second argument.
"""
model.fit(train_images, train_labels, epochs=10)

"""Compare performance on training data versus performance on test data.
"""
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)

"""If the performance on test data is worse than training data, the model is
'overfitted' -- this represents a model which has 'memorized' specifics about
the training data rather than broad characteristics applicable to new data.
"""