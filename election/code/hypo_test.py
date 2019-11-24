from pretreatment import *
from scipy import stats

data = pretreatment()
swing_state = ['MI', 'OH', 'PA', 'WI', 'FL']
blue_state = ['CA', 'NY', 'MA']
red_state = ['AL', 'TX', 'TN']
data_swing = data[data['state_abbr'].isin(swing_state)]
data_red = data[data['state_abbr'].isin(red_state)]
data_blue = data[data['state_abbr'].isin(blue_state)]

sample_red = np.random.choice(a = data_red['Clinton'], size = 100)
sample_blue= np.random.choice(a = data_blue['Clinton'], size = 100)

alpha = 0.05
t_statistic, p_value = stats.ttest_rel(a = sample_red, b = sample_blue)
print('t = ', t_statistic)
print('p = ', p_value)
if p_value <= alpha:
    print('Refuse H0')
else:
    print('Accept H1')

F = data_swing['Clinton'].var()/data_red['Clinton'].var()
df1 = len(data_swing) - 1
df2 = len(data_red) - 1
p_value_2 = 1 - 2*abs(0.5 - stats.f.cdf(F, df1, df2))
print('p = ', p_value_2)
if p_value <= alpha:
    print('Refuse H0')
else:
    print('Accept H1')

