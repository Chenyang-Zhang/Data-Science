from pretreatment import *
from sklearn.linear_model import LinearRegression
from sklearn import metrics

data = pretreatment()
swing_state = ['MI', 'OH', 'PA', 'WI', 'FL']
blue_state = ['CA', 'NY', 'MA']
red_state = ['AL', 'TX', 'TN']
data_swing = data[data['state_abbr'].isin(swing_state)]
data_red = data[data['state_abbr'].isin(red_state)]
data_blue = data[data['state_abbr'].isin(blue_state)]

linreg = LinearRegression()
linreg.fit(data_blue[['Edu_batchelors']], data_blue[['Clinton']])
y_pred = linreg.predict(data_blue[['Edu_batchelors']])
print('f(x) = ', float(linreg.intercept_), '+', float(linreg.coef_[0]), 'x')
print('RMSE = ', np.sqrt(metrics.mean_squared_error(data_blue[['Clinton']],y_pred)))
print('r_square = ', linreg.score(data_blue[['Edu_batchelors']], data_blue[['Clinton']]))
plt.plot(data_blue[['Edu_batchelors']], y_pred, 'g', alpha = 0.5)
plt.scatter(data_blue[['Edu_batchelors']], data_blue[['Clinton']], color=[0,0,1], alpha=0.5)
plt.xlabel('Betchelors Percent')
plt.ylabel('Vote rate of Clinton')
plt.show()


