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

"""Preprocess the data, this example is just the first image.
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()"""

"""Each pixel holds a value from 0 to 255, which we must reduce to a scale of 0 to 1."""
train_images = train_images / 255.0
test_images = test_images / 255.0

"""Display the first 25 images to verify preprocessing.
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()"""

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
If the performance on test data is worse than training data, the model is
'overfitted' -- this represents a model which has 'memorized' specifics about
the training data rather than broad characteristics applicable to new data.
"""
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)

"""Time to make predictions about some images with our newly trained model.
The model outputs arrays called logits holding probabilities for each possible class.
Usually these are passed to a normalization function as here.
"""
probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_images)

"""Each prediction element is an array of 10 numbers representing probabilities
that that image belongs to each of the 10 classes.
Print the first predictions for the image in our test data.
"""
#print(predictions[0])
#print(f"The model's best guess for image 1 is: {class_names[np.argmax(predictions[0])]}")
#print(f"Correct answer: {class_names[test_labels[0]]}")

# Here are some boilerplate functions to graph and visualize all 10 probabilities.

def plot_image(i, predictions_array, true_label, img):
  true_label, img = true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  true_label = true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

"""Examine the 0th & 12th images and visualize our model's predictions about them.
def visualize_predictions(i):
    plt.figure(figsize=(6,3))
    plt.subplot(1,2,1)
    plot_image(i, predictions[i], test_labels, test_images)
    plt.subplot(1,2,2)
    plot_value_array(i, predictions[i],  test_labels)
    plt.show()

visualize_predictions(0)
visualize_predictions(12)"""

"""Plot the first X test images, their predicted labels, and the true labels.
Color correct predictions in blue and incorrect predictions in red.

num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions[i], test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()"""

# Using the trained model on new inputs.
"""Grab a fresh image from the test dataset and use our model to make a prediction.
Keras is optimized for batches so we make a batch even for one member.
"""
img = test_images[1]
img = (np.expand_dims(img,0))
predictions_single = probability_model.predict(img)
plot_value_array(1, predictions_single[0], test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
#plt.show()

print(f"The model's best guess for this image is: {class_names[np.argmax(predictions[0])]}")
