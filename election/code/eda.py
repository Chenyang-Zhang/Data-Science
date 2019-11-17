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
    swing_state = ['MI', 'OH', 'PA', 'WI', 'FL']
    deepblue_state = ['CA', 'NY', 'MA']
    deepred_state = ['AL', 'TX', 'TN']
    
    sns.heatmap(data.corr(), annot = True)
    plt.title('correlation heatmap')
    plt.show()
    
    plt.subplot(221)
    data[['Female']].boxplot()
    plt.subplot(222)
    data[['White']].boxplot()
    plt.subplot(223)
    data[['Black']].boxplot()
    plt.subplot(224)
    data[['Hispanic']].boxplot()
    plt.show()

    print_result(data, ['population2014'])

    tot_votes_dem_2016 = data['votes_dem_2016'].sum()
    tot_votes_gop_2016 = data['votes_gop_2016'].sum()
    print('Total votes of Clinton:',tot_votes_dem_2016) 
    print('Total votes of Trump:',tot_votes_gop_2016)
    tot_votes_dem_2012 = data['votes_dem_2012'].sum()
    tot_votes_gop_2012 = data['votes_gop_2012'].sum()
    print('Total votes of Obama:',tot_votes_dem_2012) 
    print('Total votes of Romney:',tot_votes_gop_2012)

    #print(data[data['state_abbr'].isin(deepred_state)].sort_values(by = 'population2014'))
    print('人数最多的100个县中希拉里获胜的比例：')
    print(data.sort_values(by = 'population2014', ascending = False).head(100).result_2016.sum()/100)
    print('人数最少的100个县中希拉里获胜的比例：')
    print(data.sort_values(by = 'population2014', ascending = False).tail(100).result_2016.sum()/100)
    print(data.sort_values(by = 'Black', ascending = False).tail(100).result_2016.sum()/100)




















