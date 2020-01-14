"""
utility functions for working with DataFrames
"""

import pandas
import numpy
TEST_DF = pandas.DataFrame([1,2,3])

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