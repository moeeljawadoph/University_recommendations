# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 14:20:09 2023

@author: eljawadmo
"""

import numpy as np
import pandas as pd
import matlplotlib as plt
import seaborn as sns

import random 
from pprint import pprint


#define the  
def train_test_split(df, test_size):
    # to give the user an option of providing a percentage test_size instead of a test)size Number 
    if isinstance(test_size,float):
        test_size=round(test_size*len(df))
    # return the index of the dataframe df
    indices=df.index.tolist() 
    # draw a test_size index of indices
    test_indices = random.sample(population= indices, k = test_size)
    # extract the rows in df that has index in test_indices to get the test subset 
    test_df = df.loc[test_indices]
    #drop the rows from df that has index in test_indices to get the training subset
    train_df=df.drop(test_indices)
    return train_df, test_df

# set the seed to make your results fixed
random.seed(0)
train_df, test_df = 
