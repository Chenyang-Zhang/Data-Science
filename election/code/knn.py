from naive_bayes import *
from sklearn.neighbors import KNeighborsClassifier 


data = pretreatment()
x_train, x_test, y_train, y_test = train_test_split(data.iloc[:, 9:13], data['result_2016'], test_size = 0.3)
clf = KNeighborsClassifier(100, algorithm = 'ball_tree' )
classification_result(x_train, x_test, y_train, y_test, clf)

