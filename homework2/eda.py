import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyecharts

attribute = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']
attribute_air = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
attribute_weather = ['TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']

raw_data = pd.read_csv('PRSA_Data_Tiantan_20130301-20170228.csv')
print(raw_data.info())
print(raw_data.corr(method = 'pearson'))
print('Origin shape of the datasets:', raw_data.shape)
data = raw_data.drop(['No', 'hour', 'wd', 'station'], axis = 1)
data = data.dropna(axis = 0)
print('Processed shape of the datasets:',data.shape)

def print_result(data, attribute):
    for index in attribute:
        print('some statistical properties of %s:' % index)
        print('mean:', data[[index]].mean()[0])
        print('median:', data[[index]].median()[0])
        print('first quartile:', data[[index]].quantile(q = 0.25)[0])
        print('mode', data[[index]].mode().values[0, 0])
        print('varying range:', data[[index]].min()[0], '~', data[[index]].max()[0])
        print('max-min:', data[[index]].max()[0]-data[[index]].min()[0])
        print('standard deviation:', data[[index]].std()[0])

data_year = data.groupby(['year']).mean().drop(['month', 'day'], axis = 1)
data_month = data.groupby(['year', 'month']).mean().drop(['day'], axis = 1)
data_day = data.groupby(['year', 'month', 'day']).mean()
print('\n')
print_result(data_day.loc[(2016, 3, 1):(2016, 3, 31)], ['PM2.5'])

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)

data_year['PM2.5'].plot()
plt.title('PM2.5 concentration from 2013 to 2017')
plt.ylabel('PM2.5 concentration ug/m^3')
plt.ylim(0, 100)

ax2 = fig.add_subplot(2, 2, 2)
data_month['PM2.5'].plot()
plt.title('PM2.5 concentration from 2013.3 to 2017.2')
plt.ylabel('PM2.5 concentration ug/m^3')

ax3 = fig.add_subplot(2, 2, 3)
data_day['PM2.5'].plot(kind = 'scatter')
plt.title('PM2.5 concentration from 2013.3.1 to 2017.2.28')
plt.ylabel('PM2.5 concentration ug/m^3')

ax4 = fig.add_subplot(2, 2, 4)
data_day.loc[(2016, 11):(2016, 12)]['PM2.5'].plot()
plt.title('PM2.5 concentration from 2016.11.1 to 2016.12.31')
plt.ylabel('PM2.5 concentration ug/m^3')

plt.subplots_adjust(wspace = 0.1, hspace = 0.5)
plt.show()

data_day[data_day[['PM2.5']]<75] = 0
data_day[data_day[['PM2.5']]>=75] = 1
pollute_day = data_day[['PM2.5']].sum()
print(data_day.shape)
print(pollute_day)
