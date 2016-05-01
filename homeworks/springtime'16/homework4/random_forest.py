__author__ = 'anastasiiakorosteleva'

import numpy as np
from scipy.ndimage import imread
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics.classification import accuracy_score

def get_images(dir_name):
    images = []
    for file_name in os.listdir(dir_name):
        x = imread(dir_name + "/" + file_name, flatten=True)
        x.shape = (10000, )
        images.append(x)
    images = np.array(images)
    return images


cats = get_images("cats")
dogs = get_images("dogs")
np.random.shuffle(cats)
np.random.shuffle(dogs)

train_cats = cats[:200, ]
validate_cats = cats[200: ]

train_dogs = dogs[:200, ]
validate_dogs = dogs[200: ]

train = np.concatenate((train_cats, train_dogs))
validate = np.concatenate((validate_cats, validate_dogs))

train_y = np.array((np.ones(200), np.zeros(200)))
train_y.shape = (400, )

def four_algorythms(algorythm, n_est):
    if algorythm == "RandomForestClassifier":
        prediction = RandomForestClassifier(n_estimators=n_est)
    if algorythm == "ExtraTreesClassifier":
        prediction = ExtraTreesClassifier(n_estimators=n_est)
    if algorythm == "AdaBoostClassifier":
        prediction = AdaBoostClassifier(n_estimators=n_est)
    if algorythm == "GradientBoostingClassifier":
        prediction = GradientBoostingClassifier(n_estimators=n_est)

    prediction = prediction.fit(train, train_y)
    validate_y = np.concatenate((np.ones(50), np.zeros(50)))
    predicted_y = prediction.predict(validate)
    return(accuracy_score(validate_y, predicted_y))

print('\t'+'n_estimators')
number_est = ["Algorythm", 10, 20, 40, 80, 100, 150, 200, 300, 400, 500, 1000]
print('\t'.join(map(str, number_est)))
for algorythm in ["RandomForestClassifier",
                  "ExtraTreesClassifier",
                  "AdaBoostClassifier",
                  "GradientBoostingClassifier"]:
    spisok = list()
    spisok.append(algorythm)
    for n_est in [10, 20, 40, 80, 100, 150, 200, 300, 400, 500, 1000]:
        i = 1
        accuracy = 0
        while i != 11:
            accuracy += (four_algorythms(algorythm, n_est)/10)
            i+=1
        spisok.append(accuracy)
    print('\t'.join(map(str, spisok)))
