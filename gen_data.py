from PIL import Image
import os, glob, sys
import numpy as np
from sklearn import model_selection

save_data = sys.argv[1]

classes = ['apple', 'cherry', 'grape']
num_classes = len(classes)
image_size = 50

# 画像の読み込み
X_train = []
X_test = []
y_train = []
y_test = []

file_num = 600
for index, classlabel in enumerate(classes):
  photos_dir = "./" + classlabel
  files = glob.glob(photos_dir + "/*.jpg")
  if len(files) < file_num:
    file_num = len(files)

testdata_num = 100
for index, classlabel in enumerate(classes):
  photos_dir = "./" + classlabel
  files = glob.glob(photos_dir + "/*.jpg")
  for i, file in enumerate(files):
    if i >= file_num:
      break

    image = Image.open(file)
    image = image.convert("RGB")
    image = image.resize((image_size, image_size))
    data = np.asarray(image)

    if i <= testdata_num:
      X_test.append(data)
      y_test.append(index)

    else:
      for angle in range(-20, 20, 5):
        img_r = image.rotate(angle)
        data = np.asarray(img_r)
        X_train.append(data)
        y_train.append(index)
        
        img_trans = img_r.transpose(Image.FLIP_LEFT_RIGHT)
        data = np.asarray(img_trans)
        X_train.append(data)
        y_train.append(index)

X_train = np.array(X_train)
X_test = np.array(X_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

xy = (X_train, X_test, y_train, y_test)
np.save(save_data, xy)
