from naive_bayes import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

data = pretreatment()
x = data.iloc[:, 9:13]
y = data['result_2016']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)
my_tree = DecisionTreeClassifier(max_depth = 5)
classification_result(x_train, x_test, y_train, y_test, my_tree)
print(pd.DataFrame({'feature':data.columns[9:13], 'importance':my_tree.feature_importances_}))
plt.figure(figsize = (28, 18))
#plot_tree(my_tree, fontsize = 12, feature_names = data.columns[9:13],class_names = ['Clinton', 'Trump'])
plt.show()
