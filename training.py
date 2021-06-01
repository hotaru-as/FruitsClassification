from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.keras.utils import to_categorical
import tensorflow
import numpy as np
import matplotlib.pyplot as plt
from model import Model
import sys

classes = ['apple', 'cherry', 'grape']
num_classes = len(classes)
image_size = 50

load_data = sys.argv[1] # fruits.npy

def main():
  X_train, X_test, y_train, y_test = np.load(load_data, allow_pickle=True)
  print(X_train.shape)
  print(X_test.shape)
  X_train = X_train.astype("float") / 255
  X_test = X_test.astype("float") / 255
  y_train = to_categorical(y_train, num_classes)
  y_test = to_categorical(y_test, num_classes)

  model = model_train(X_train, y_train)
  model_eval(model, X_test, y_test)

def model_train(X_train, y_train):
  epochs = 100
  batch_size = 32

  models = Model()
  model = models.create_model()

  history = model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)

  # モデルの保存
  model.save('./fruits_model.h5')

  x = range(epochs)

  fig = plt.figure()
  plt.plot(x, history.history['accuracy'], label='accuracy')
  plt.title('accuracy')
  plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
  plt.show()
  fig.savefig('acc.png')

  fig = plt.figure()
  plt.plot(x, history.history['loss'], label='loss')
  plt.title('loss')
  plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
  plt.show()
  fig.savefig('loss.png')

  return model

def model_eval(model, X, y):
  scores = model.evaluate(X, y, verbose=1)
  print('test loss: ', scores[0])
  print('test Accuracy: ', scores[1])

if __name__ == "__main__":
  main()
