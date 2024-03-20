# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 23:24:05 2023

@author: eljawadmo
"""

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# create a function that would take the first 8 columns as features and predict the label, which can be either column 10, or column 11
# the function should begin by splitting the dataset to train and test datasets
# verify if their is any corroleation between the grades columns (which shouldn't be the case) done in the visualize script and no correlation between the grades was found
# 

def train_test_split_df(df,col='Suggestion Based on Top 4 grades'):
    #one hot encoding of the is_sucess column
    df=pd.concat([df,pd.get_dummies(df["is_sucess"])],axis=1)
    #drop the orginal column
    df=df.drop(["is_sucess"],axis=1)
    #rename the 0 and 1 catagories to fail and sucess
    df = df.rename(columns={0: "fail", 1: "success"})
    grades= ['Math Grade', 'Physics Grade', 'Biology Grade', 'Chemistry Grade',
           'English Grade', 'History Grade', 'Economy Grade', 'Geography Grade']
    binned_grade=bin_grades(df[grades])
    #features = grades+["fail", "success"]
    #Select the features, that are presented in column 0 to 8 then 10,11
    X=pd.concat([binned_grade,df[["fail","success"]]],axis=1)
    #select the label
    y = df[col]
    
    # Split the features and labels to two sets, one for training and the other for test.
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=25, train_size=0.8,stratify=y)
    
    return X_train, X_test, y_train, y_test

# Try binning of grades or standardscaler for logistic regression
def bin_grades(df):
    """
    bin the grades columns to the bins specified by the bin_edges list defined within the function
    
    Parameters
    ----------
    df: DataFrame
        The DataFrame containing the columns of grades to be binned
    
    Returns
    -------
    grades_binned_df: DataFrame
        The binned dataframe having the same columns as the df input dataframe
        
        
    Examples
    --------
    input:
        df= 
         Math Grade | Physics Grade | Biology Grade | Chemistry Grade | English Grade | History Grade | Economy Grade | Geography Grade
         93 | 70 | 85 | 75 | 83 | 88 | 65 | 55
         63 | 73 | 58 | 45 | 80 | 68 | 75 | 85
         84 | 85 | 82 | 85 | 60 | 88 | 82 | 63
    
    output:
    
        grades_binned_df=
     Math Grade | Physics Grade | Biology Grade | Chemistry Grade | English Grade | History Grade | Economy Grade | Geography Grade
     7 | 3 | 6 | 4 | 5 | 6 | 2 | 0
     1 | 3 | 0 | 0 | 5 | 2 | 4 | 6
     5 | 6 | 5 | 6 | 1 | 6 | 5 | 1
    """
    bin_edges = [40, 59, 64, 69, 74, 79, 84, 89, 94, 100]
    # Digitize the grades based on the custom bin edges
    grades_binned = np.digitize(df, bin_edges, right=True) - 1
    # convert to dataframe
    grades_binned_df = pd.DataFrame(grades_binned, columns=df.columns)
    return grades_binned_df


# check the decision Tree Feature Importance
def get_feature_importance(X_train, y_train):
    """
    get the feature importance from a decision tree model
    Parameters
    ----------
    X_train: DataFrame
        The DataFrame containing the features of the training data that will be passed to the decision tree model
    
    y_train: DataFrame
        The DataFrame containing the labels of the training data that will be passed to the decision tree model
    """
    dt_classifier = DecisionTreeClassifier(random_state=42)
    dt_classifier.fit(X_train,y_train)
    #Access the feature imortances
    feature_importances = dt_classifier.feature_importances_
    
    # Create a DataFrame to display the feature importances
    feature_importance_df = pd.DataFrame({'Feature': X_train.columns, 'Importance': feature_importances})
    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
    
    return feature_importance_df


def draw_feature_importance(feature_importance_df, path=None):
    """
    draw the feature importance vs features as a histogram
    Parameters
    ----------
    feature_importance_df: DataFrame
        A DataFrame that has two columns one is Feature and the other is Importance 
    
    """
    plt.barh(feature_importance_df['Feature'], feature_importance_df['Importance'])
    plt.xlabel('Importance')
    plt.title('Feature Importances')
    if path is not None:
        os.makedirs(path, exist_ok=True) 
        fig_path = os.path.join(path, 'Feature Importance.png')
        plt.savefig(fig_path)
    plt.show()

