# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 15:48:35 2023

@author: eljawadmo
"""
from src.data import create_clean_data, threshold, nsample
from src.visualilzation import plotPerColumnDistribution, plot_correlation_between_grades
#from models import 

import pandas as pd
import numpy as np
#from src import data
#from src.data.generate_data import create_clean_data, nsample, threshold



#df = create_clean_data(nsample,threshold,True)
df = pd.read_csv("./data/raw/Generated_data_10000.csv")

#plotting distribution by role:
plotPerColumnDistribution(df, 'Suggestion Based on Top 4 grades')
plotPerColumnDistribution(df, 'Suggestion Based on Mean')

plot_correlation_between_grades(df)





