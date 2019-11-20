import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from pretreatment import pretreatment
from naive_bayes import classification_result

if __name__ == '__main__':
    data = pretreatment()
    x_train, x_test, y_train, y_test = train_test_split(np.array(data)[:, 9:13], np.array(data)[:, 19].astype(int), test_size = 0.3)
    clf = GaussianNB()
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    classification_result(x_test, y_test, y_pred)

