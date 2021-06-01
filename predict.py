from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.keras.utils import to_categorical
import tensorflow
import numpy as np
from PIL import Image
from sklearn import model_selection
import sys
from model import Model

classes = ['apple', 'cherry', 'grape']
num_classes = len(classes)
image_size = 50

def build_model():
  models = Model()
  model = models.create_model()

  model = load_model('./fruits_model.h5')

  return model


def main():
  image = Image.open(sys.argv[1])
  image = image.convert('RGB')
  image = image.resize((image_size, image_size))
  data = np.asarray(image)
  X = []
  X.append(data)
  X = np.array(X)
  model = build_model()

  result = model.predict([X])[0]
  predicted = result.argmax()
  percentage = int(result[predicted] * 100)
  print("{0} ({1}%)".format(classes[predicted], percentage))

if __name__ == "__main__":
    main()