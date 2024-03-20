# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 00:38:16 2023

@author: Mohammad El Jawad

The file will contain the files used to visualize the generated_data...
"""

import matplotlib.pyplot as plt
import seaborn as sns
import os


# Distribution graphs (histogram/bar graph) of column data
def plotPerColumnDistribution(df, column_name,nbins=None):
    """
    Plot the unique values in a column on x_axis, and their value count on y_axis
    
    Parameters
    ----------
    df: DataFrame
        The Dataframe where the column distribution is to be plotted
    column_name: str
        The Column whose distribution is to be plotted
    nbins: int 
        how many values you would like to have on the x-axis (default= None, include all unique values)
        
    Returns
    -------
    axes:
        a plot with unique values on x_axis and value count on y_axis. When nbins = None, or >=15 the xtickt will be removed 
        
    
    """
    value_counts = df[column_name].value_counts()
    count = len(value_counts)
    plt.bar(value_counts[1:nbins].index,value_counts[1:nbins].values)
    if (nbins is None) or (nbins>15):
        plt.xticks([])
    else:
        plt.xticks(rotation = 90)
    nbins = count if nbins is None else nbins
    plt.ylabel('Count')
    plt.title(f'{column_name} {nbins} out of ({count}) majors')
    plt.show()


def check_generated_grade_distribution(df,path=None):
    """
    Plot and Save (optional) the grade distribution that were generated
    
    Parameters
    ----------
    df: DataFrame
        The Dataframe where the column distribution is to be plotted
    
    path: str
        specify the path where the plot is to be saved as a png images.
    
    Returns
    -------
    axes: axes
        a  4 col x 2 rows plot showing the grade distribution per course of the  
        
    """

    figs, axes = plt.subplots(2, 4, figsize=(10, 12))
    axes = axes.flatten()

    for i, col in enumerate(df.columns[:8]):
        ax = axes[i]
        counts, bins, _ = ax.hist(df[col], bins=range(40, 105, 5), edgecolor='black')
        ax.set_xlabel('Grade')
        ax.set_ylabel('Frequency')
        ax.set_title('Distribution of Grades in {}\n for {} Data Points'.format(col, len(df[col])))

    plt.tight_layout()

  # Save figures if path parameter is provided
    if path is not None:
        os.makedirs(path, exist_ok=True)
        for i, col in enumerate(df.columns[:8]):
            fig_path = os.path.join(path, f'{col}_histogram_{len(df[col])}_points.png')
            figs[i].savefig(fig_path)

    plt.show()
    
def plot_correlation_between_grades(df,path=None):
    grades_columns = df.iloc[:, :8]
    correlation_matrix = grades_columns.corr()
    htMap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    #Format the tick labels for the x and y axes.
    htMap.set_xticklabels(htMap.get_xmajorticklabels(), size = 10, rotation = 90)
    htMap.set_yticklabels(htMap.get_ymajorticklabels(), size = 10, rotation = 0)
    plt.title('Correlation Matrix')
    
    if path is not None:
        os.makedirs(path, exist_ok=True) 
        fig_path = os.path.join(path, f'correlation_matrix_for_{len(df)}_points.png')
        plt.savefig(fig_path)
    
    plt.show()
    