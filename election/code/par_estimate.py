from scipy import stats
from pretreatment import *

data = pretreatment()
lst = []
for i in range(1000):
    sample = np.random.choice(a = data['population2014'], size = 100)
    lst.append(sample.mean())
sns.distplot(pd.DataFrame(lst))
plt.show()
print(np.array(lst).mean())

def MakeConfidenceInterval(sample_size, data, alpha):
    sample = np.random.choice(a = data, size = sample_size)
    sigma = sample.std()/np.sqrt(sample_size)
    return stats.t.interval(alpha = alpha, df = sample_size -1,
            loc = sample.mean(), scale = sigma)

print('Confidence interval with confidence level of 95%:', 
        MakeConfidenceInterval(1000, data['population2014'], 0.95))

temp = 0
for i in range(10000):
    interval = MakeConfidenceInterval(1000, data['population2014'], 0.95)
    if (data['population2014'].mean() >= interval[0]) &(data['population2014'].mean() <= interval[1]):
        temp += 1
print(temp/10000)





