"""
lambdata - a collection of data science helper functions
"""

import pandas as pd
import numpy as np

#sample code
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))

def get_feature_names(df):
     '''
     Pass in Dataframe to retrieve a list
     of columns 
     '''
     return df.columns

def null_summary(df):
    '''
    Pass in Dataframe to get list of nulls
    '''
    return df.isnull().sum()