__author__ = 'anastasiiakorosteleva'
import numpy as np
# x = np.array([[1,2,3], [4,5,6]])
# print(x.dtype)
# # print(x)
# # y = np.ones((3,3))
# # print(y)
# # y.shape = (3,3)
# # print(y)
# y = np.arange(0,12)
# y.shape = (4,3)
# print(y + np.array([1,0,2]))
#
# import timeit
# setup = """
# import numpy as np
# k = 10 * 1000 * 1000
# """
# x = timeit.timeit("y = np.random.normal(0,2,k)",
#                   setup, number=1)
# print(x)
#
# setup = """
# from random import gauss
# k = 10 * 1000 * 1000
# """
# x = timeit.timeit("y = [gauss(0.0, 2.0) for i in range(k)]",
#                   setup, number=1)
# print(x)
from scipy.ndimage import imread
x = imread("faces/253_0001.jpg", flatten=True)

import os

def get_images(dir_name):
    images = []
    for file_name in os.listdir(dir_name):
        x = imread(dir_name + "/" + file_name, flatten=True)
        x.shape = (10000, )
        images.append(x)
    images = np.array(images)
    return images

faces = get_images("faces")
non_faces = get_images("non_faces")
np.random.shuffle(faces)
np.random.shuffle(non_faces)

train_faces = faces[:350, ]
validate_faces = faces[350:, ]
train_non_faces = non_faces[:350, ]
validate_non_faces = non_faces[350:, ]
train = np.concatenate((train_faces, train_non_faces))
validate = np.concatenate((validate_faces, validate_non_faces))
train_y = np.array((np.ones(350), np.zeros(350)))
train_y.shape = (700, )

from sklearn.ensemble import RandomForestClassifier, \
    ExtraTreesClassifier
random_forest = RandomForestClassifier(n_estimators=20)
print(train.shape, train_y.shape)
random_forest = random_forest.fit(train, train_y)

importances = random_forest.feature_importances_
importances = importances.reshape((100, 100))

plt.matshow(importances, cmap=plt.cm.hot)
plt.title("Pixel importances with forest of tree")
