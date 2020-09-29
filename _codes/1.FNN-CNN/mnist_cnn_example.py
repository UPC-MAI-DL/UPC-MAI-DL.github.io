from __future__ import division
import keras
import tensorflow as tf
print( 'Using Keras version', keras.__version__)
from keras.datasets import mnist
#Load the MNIST dataset, already provided by Keras
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#Check sizes of dataset
print( 'Number of train examples', x_train.shape[0])
print( 'Size of train examples', x_train.shape[1:])

#Adapt the data as an input of a fully-connected (flatten to 1D)
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

#Normalize data
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train = x_train / 255
x_test = x_test / 255

#Adapt the labels to the one-hot vector syntax required by the softmax
from keras.utils import np_utils
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

#MNIST resolution
img_rows, img_cols, channels = 28, 28, 1
input_shape = (img_rows, img_cols, channels)
#Reshape for input
x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, channels)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, channels)

#Define the NN architecture
from keras.models import Sequential
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Flatten
#Two hidden layers
model = Sequential()
model.add(Conv2D(8, 3, 3, activation='relu', input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(16, 3, 3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(8, activation='relu'))
model.add(Dense(10, activation=(tf.nn.softmax)))

#Model visualization
#We can plot the model by using the ```plot_model``` function. We need to install *pydot, graphviz and pydot-ng*.
#from keras.util import plot_model
#plot_model(model, to_file='model.png', show_shapes=true)

#Compile the NN
model.compile(optimizer='sgd',loss='categorical_crossentropy',metrics=['accuracy'])

#Start training
history = model.fit(x_train,y_train,batch_size=128,epochs=20, validation_split=0.15)

#Evaluate the model with test set
score = model.evaluate(x_test, y_test, verbose=0)
print('test loss:', score[0])
print('test accuracy:', score[1])

##Store Plots
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#Accuracy plot
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train','val'], loc='upper left')
plt.savefig('mnist_fnn_accuracy.pdf')
plt.close()
#Loss plot
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train','val'], loc='upper left')
plt.savefig('mnist_fnn_loss.pdf')

#Confusion Matrix
from sklearn.metrics import classification_report,confusion_matrix
import numpy as np
#Compute probabilities
Y_pred = model.predict(x_test)
#Assign most probable label
y_pred = np.argmax(Y_pred, axis=1)
#Plot statistics
print( 'Analysis of results' )
target_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(classification_report(np.argmax(y_test,axis=1), y_pred,target_names=target_names))
print(confusion_matrix(np.argmax(y_test,axis=1), y_pred))

#Saving model and weights
from keras.models import model_from_json
model_json = model.to_json()
with open('model.json', 'w') as json_file:
        json_file.write(model_json)
weights_file = "weights-MNIST_"+str(score[1])+".hdf5"
model.save_weights(weights_file,overwrite=True)

#Loading model and weights
#json_file = open('model.json','r')
#model_json = json_file.read()
#json_file.close()
#model = model_from_json(model_json)
#model.load_weights(weights_file)
