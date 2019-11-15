import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats

raw_data = pd.read_csv('PRSA_Data_Tiantan_20130301-20170228.csv')
data = raw_data.drop(['No', 'hour', 'wd', 'station'], axis = 1)
data = data.dropna(axis = 0)
data = data["PM2.5"].tolist()
np.random.seed(1234)
data = np.random.choice(a = data, size = 2000) #reduce sample size

#onesided t-test
print("the null hypothesis H0: the mean of PM2.5 concentration is less than 75ug/m^3")
t_statistic, p_value = stats.ttest_1samp(a = data, popmean = 75)
p_value_onesided = p_value / 2 #p_value is two-sided test result
print("the t-statistic generated from sample = %f" % t_statistic )
print("the p value of onesided t-test = %f" % p_value_onesided)

#plot t-distribution 
df = len(data) - 1
x = np.linspace(stats.t.ppf(0.00000001, df), stats.t.ppf(0.99999999, df), 100)
plt.plot(x, stats.t.pdf(x, df))
plt.plot((t_statistic, t_statistic), (-0.01, 0.4), '-.r')
plt.legend(('t distribution', 'calculated t'))

x_025 = stats.t.ppf(0.025, df)
plt.plot((x_025, x_025), (-0.01, 0.4), '--g') #left threshold
x_975 = stats.t.ppf(0.975, df)
plt.plot((x_975, x_975), (-0.01, 0.4), '--g') #right threshold

rect1 = plt.Rectangle((x_025, 0), x_975*2, 0.5, color = 'g', alpha = 0.25)
plt.gca().add_patch(rect1)

rect2 = plt.Rectangle((x_975, 0), 5, 0.5, color = 'r', alpha = 0.25)
plt.gca().add_patch(rect2)

rect3 = plt.Rectangle((x_025, 0), -5, 0.5, color = 'r', alpha = 0.25)
plt.gca().add_patch(rect3)

plt.text(x_025, 0.4, 'accept region')
plt.savefig('test_result.png')
plt.show()


alpha = 0.05
if t_statistic > 0 and p_value <= alpha:
    print("Refuse H0, accept H1")
else:
    print("Accept H0, refuse H1")

