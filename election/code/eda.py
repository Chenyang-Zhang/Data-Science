import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pretreatment import pretreatment

def print_result(data, attribute):
    for index in attribute:
        print('Some statistical properties of %s:' % index)
        print('======================================')
        print('mean:', data[[index]].mean()[0])
        print('median:', data[[index]].median()[0])
        print('first quartile:', data[[index]].quantile(q = 0.25)[0])
        print('third quartile:', data[[index]].quantile(q = 0.75)[0])
        print('mode', data[[index]].mode().values[0, 0])
        print('varying range:', data[[index]].min()[0], '~', data[[index]].max()[0])
        print('max-min:', data[[index]].max()[0]-data[[index]].min()[0])
        print('standard deviation:', data[[index]].std()[0])
        print('======================================')

if __name__ == '__main__':
    
    data = pretreatment()
    print('Basic information of the datasets after pretreatment:')
    print(data.info())

    swing_state = ['MI', 'OH', 'PA', 'WI', 'FL']
    deepblue_state = ['CA', 'NY', 'MA']
    deepred_state = ['AL', 'TX', 'TN']
    
    print(data.describe())
    heatmap_col = ['Clinton', 'Trump', 'population2014', 'age65plus', 'Female', 'White', 'Black', 
            'Hispanic', 'Edu_batchelors', 'Income', 'Poverty']
    plt.figure(figsize = (13, 10), dpi = 100)
    sns.heatmap(data[heatmap_col].corr(), annot = True)
    plt.title('correlation heatmap')
    plt.show()

    pairplot_col = ['Clinton', 'Trump', 'population2014', 
            'age65plus', 'White', 'Black', 'Edu_batchelors']
    sns.pairplot(data[pairplot_col], diag_kind = 'kde',  
            plot_kws = {'alpha': 0.3})
    plt.show()

    tot_votes_dem_2016 = data['votes_dem_2016'].sum()
    tot_votes_gop_2016 = data['votes_gop_2016'].sum()
    print('Total votes of Clinton:',tot_votes_dem_2016) 
    print('Total votes of Trump:',tot_votes_gop_2016)
    tot_votes_dem_2012 = data['votes_dem_2012'].sum()
    tot_votes_gop_2012 = data['votes_gop_2012'].sum()
    print('Total votes of Obama:',tot_votes_dem_2012) 
    print('Total votes of Romney:',tot_votes_gop_2012)
    print('==================================')
    
    plt.subplot(241)
    data[['Female']].boxplot()
    plt.subplot(242)
    data[['White']].boxplot()
    plt.subplot(243)
    data[['Black']].boxplot()
    plt.subplot(244)
    data[['Hispanic']].boxplot()
    plt.subplot(245)
    data[['age65plus']].boxplot()
    plt.subplot(246)
    data[['Edu_batchelors']].boxplot()
    plt.subplot(247)
    data[['Income']].boxplot()
    plt.subplot(248)
    data[['Poverty']].boxplot()
    plt.show()

    print_result(data, ['population2014'])


    #print(data[data['state_abbr'].isin(deepred_state)].sort_values(by = 'population2014'))
    print('人数最多的100个县中希拉里获胜的比例：')
    print(data.sort_values(by = 'population2014', ascending = False).head(100).result_2016.sum()/100)
    print('人数最多的100个县占美国总人口的比例：')
    print(data.sort_values(by = 'population2014', ascending = False).head(100).population2014.sum()/data.population2014.sum())
    print('人数最少的100个县中希拉里获胜的比例：')
    print(data.sort_values(by = 'population2014', ascending = False).tail(100).result_2016.sum()/100)
    print('女性比例最多的100个县中希拉里获胜的比例：')
    print(data.sort_values(by = 'Female', ascending = False).head(100).result_2016.sum()/100)
    print('黑人比例最多的100个县中希拉里获胜的比例：')
    print(data.sort_values(by = 'Black', ascending = False).head(100).result_2016.sum()/100)
    print('白人比例最多的100个县中希拉里获胜的比例：')
    print(data.sort_values(by = 'White', ascending = False).head(100).result_2016.sum()/100)
    print('受教育程度最高的100个县中希拉里获胜的比例：')
    print(data.sort_values(by = 'Edu_batchelors', ascending = False).head(100).result_2016.sum()/100)

    #print(data.groupby('state_abbr').sum())

    print(data.sort_values(by = 'population2014', ascending = False).head(300).population2014.sum()/data.population2014.sum())
    county_population500 = data.sort_values(by = 'population2014', ascending = False).head(300)
    Clinton_bigwin = [1 if x - y >= 0.3 else 0 for x,y in np.array(county_population500[['Clinton', 'Trump']])]
    Trump_bigwin = [1 if y - x >= 0.3 else 0 for x,y in np.array(county_population500[['Clinton', 'Trump']])]
    print(sum(Clinton_bigwin), sum(Trump_bigwin))
    



















