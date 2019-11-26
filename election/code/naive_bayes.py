from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from pretreatment import *

def classification_result(x_train, x_test, y_train, y_test, clf):
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    result = pd.DataFrame(np.transpose([y_test, y_pred]), columns = {'true_result', 'predict_result'})
    print(result[result['true_result'] != result['predict_result']])
    print('Classification correct rate:', accuracy_score(y_test, y_pred) )
    print('Confusion matrix:',confusion_matrix(y_pred, y_test), sep = '\n')
    print('Classification report:', classification_report(y_pred, y_test), sep = '\n')

if __name__ == '__main__':
    data = pretreatment()
    feature_col = ['population2014', 'White', 'Black', 'Edu_batchelors', 'age65plus', 'Poverty']
    x_train, x_test, y_train, y_test = train_test_split(data[feature_col], data['result_2016'], test_size = 0.3)
    clf = GaussianNB()
    classification_result(x_train, x_test, y_train, y_test, clf)

