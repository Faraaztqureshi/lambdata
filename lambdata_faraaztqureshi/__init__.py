"""
lambdata - a collection of data science helper functions
"""

import pandas as pd
import numpy as np

# sample code
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))

"""
Class to help clean data
"""


class Data_cleaning():
    '''This class will contains methods that can be used
    in order to clean and analyze data
    '''

    def __init__(self):
        pass

    def shape(self, df):
        ''' Pass in DataFrame and get result of rows and columns
        '''
        return df.shape

    def get_feature_names(self, df):
        '''
        Pass in Dataframe to retrieve a list
        of columns
        '''
        return df.columns

    def null_summary(self, df):
        '''
        Pass in Dataframe to get list of nulls
        '''
        return df.isnull().sum()

    def search_string(self, df, column_name, search_word):

        '''Inputs are df, column_name and search_word
        df is the DataFrame you are working with
        column_name is the name of the column as a string
        search_word is string version of the word
        you are searching for
        '''
        return df[df[column_name].str.contains(search_word)]
