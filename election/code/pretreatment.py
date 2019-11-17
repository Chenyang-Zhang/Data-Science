import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

def pretreatment():
    raw_data = pd.read_csv('../votes.csv')
    print('Basic information of the datasets:')
    print(raw_data.info())
    #select some interested attribute 
    columns = ['state_fips', 'state_abbr', 'county_name', 'population2014','votes_dem_2016', 'votes_gop_2016','votes_dem_2012', 'votes_gop_2012',  'age65plus', 'SEX255214','White','Black','Hispanic', 'Edu_batchelors', 'Income', 'Poverty', 'Clinton_Deviation', 'Trump_Deviation']
    data = raw_data[columns]
    data = data.rename(columns = {'SEX255214':'Female'})
    data = data.set_index('county_name')
    print(data.isnull().sum()) #check whether there is missing values
    #data.dropna()
    result_2016 =[1 if x > y else 0 for x, y in np.array(data[['votes_dem_2016', 'votes_gop_2016']])] 
    result_2012 =[1 if x > y else 0 for x, y in np.array(data[['votes_dem_2012', 'votes_gop_2012']])] 
    data.loc[:,'result_2016'] = result_2016
    data.loc[:,'result_2012'] = result_2012
    data = data.sort_values(by = ['state_fips','population2014'], ascending = [True, False])
    print('======================================================')
    print('Basic information of the datasets after pretreatment:')
    print(data.info())
    #print(data)
    return data



if __name__ == '__main__':
    pretreatment();
