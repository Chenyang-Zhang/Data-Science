from scipy import stats
from pretreatment import *

data = pretreatment()
swing_state = ['MI', 'OH', 'PA', 'WI', 'FL']
blue_state = ['CA', 'NY', 'MA']
red_state = ['AL', 'TX', 'TN']
data_swing = data[data['state_abbr'].isin(swing_state)]
data_red = data[data['state_abbr'].isin(red_state)]
data_blue = data[data['state_abbr'].isin(blue_state)]

pnt_estimate_red = []
pnt_estimate_blue = []
pnt_estimate_swing = []
for i in range(1000):
    sample = np.random.choice(a = data_red['Trump'], size = 100)
    pnt_estimate_red.append(sample.mean())
for i in range(1000):
    sample = np.random.choice(a = data_blue['Trump'], size = 100)
    pnt_estimate_blue.append(sample.mean())
for i in range(1000):
    sample = np.random.choice(a = data_swing['Trump'], size = 100)
    pnt_estimate_swing.append(sample.mean())
sns.distplot(pd.DataFrame(pnt_estimate_red), kde_kws={"color": 'r'}, color = 'r')
sns.distplot(pd.DataFrame(pnt_estimate_blue),  kde_kws={"color": [0,0,1]}, color = [0,0,1])
sns.distplot(pd.DataFrame(pnt_estimate_swing), kde_kws = {'color': [1,0,1]}, color = [1,0,1])
plt.legend(['red_state', 'blue_state', 'swing_state'], fontsize = 15)
plt.grid(linestyle = '--')
plt.xlabel('Vote rate of Trump')
plt.show()
print('Mean point estimatation in red states', 
        np.array(pnt_estimate_red).mean())
print('Mean point estimatation in blue states', 
        np.array(pnt_estimate_blue).mean())
print('Mean point estimatation in swing states', 
        np.array(pnt_estimate_swing).mean())

def MakeConfidenceInterval(sample_size, data, alpha):
    sample = np.random.choice(a = data, size = sample_size)
    sigma = sample.std()/np.sqrt(sample_size)
    return stats.t.interval(alpha = alpha, df = sample_size -1,
            loc = sample.mean(), scale = sigma)
print('Confidence interval in red state:', 
        MakeConfidenceInterval(100, data_red['Clinton'], 0.95))
print('Confidence interval in blue state:', 
        MakeConfidenceInterval(100, data_blue['Clinton'], 0.95))
print('Confidence interval in swing state:', 
        MakeConfidenceInterval(100, data_swing['Clinton'], 0.95))

temp = 0
for i in range(10000):
    interval = MakeConfidenceInterval(100, data_blue['Clinton'], 0.95)
    if (data_blue['Clinton'].mean() >= interval[0]) &(data_blue['Clinton'].mean() <= interval[1]):
        temp += 1
print(temp/10000)




