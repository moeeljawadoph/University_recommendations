# -*- coding: utf-8 -*-
"""
The file contains all the custom functions created in this project
"""

import random
import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




def generate_Grades(n_samples=1000):
    """
    Generate n_samples rows with courses as columns
    
    Parameters
    ----------
    n_samples: int
        The number of sample to generate
    
    Returns
    -------
    df: DataFrame
        DataFrame with Student ID as index and Math,Physics, Biology, Chemistry, English, History, Economy and Geography as columns
        
        
    Examples
    --------
    input:
        n_samples=3
    
    output:
    
        df=
    Student ID | Math Grade | Physics Grade | Biology Grade | Chemistry Grade | English Grade | History Grade | Economy Grade | Geography Grade
    1 | 93 | 70 | 85 | 75 | 83 | 88 | 65 | 55
    2 | 63 | 73 | 58 | 45 | 80 | 68 | 75 | 85
    3 | 84 | 85 | 82 | 85 | 60 | 88 | 82 | 63
    """
    student_ids = range(n_samples)
    grades = []
    for _ in range(n_samples):
        math_grade = random.randint(40, 100)
        physics_grade = random.randint(40, 100)
        biology_grade = random.randint(40, 100)
        chemistry_grade = random.randint(40, 100)
        english_grade = random.randint(40, 100)
        history_grade = random.randint(40, 100)
        economy_grade = random.randint(40, 100)
        geography_grade = random.randint(40, 100)
     #   major_recommendation = random.choice(['Engineering', 'Medicine', 'Business', 'Computer Science'])
    
        grades.append([
            math_grade, physics_grade, biology_grade, chemistry_grade, english_grade,
            history_grade, economy_grade, geography_grade
        ])
    
    df = pd.DataFrame(grades, columns=[
        'Math Grade', 'Physics Grade', 'Biology Grade', 'Chemistry Grade', 'English Grade',
        'History Grade', 'Economy Grade', 'Geography Grade'
    ])
    
    df.insert(0, 'Student ID', student_ids)
    df.set_index('Student ID', inplace=True)
    return df


def process_student_grades(df):
    """
    For each student in the dataframe, calculate top 4 grades and mean - variance.
    
    Parameters
    ----------
     df: DataFrame
        DataFrame with Student ID as index and Grades
    
    Returns
    -------
    grades_dict: dict 
        dict of dict with student id as key and values of dict where courses name as keys and grades as values.
    top_grades_dict: dict 
        dict of dict with student id as key and values of dict where courses name as keys and grades as values
    is_sucess: dict 
        returns 0 or 1, 0 if the sum of grades of a student is <480 and 1 if the grades >= 480.
    above_average_dict: dict 
        dictionary of courses that had a grade that is higher than the average minus standard deviation of the student.
        
    Examples
    --------
    Input:
        df= 
    Student ID | Math Grade | Physics Grade | Biology Grade | Chemistry Grade | English Grade | History Grade | Economy Grade | Geography Grade
    1 | 93 | 70 | 85 | 75 | 83 | 88 | 65 | 55
    2 | 63 | 73 | 58 | 45 | 80 | 68 | 75 | 85
    3 | 84 | 85 | 82 | 85 | 60 | 88 | 82 | 63
    
    Output:
        grades_dict = {1:{'Math':93, 'Physics':70, 'Biology':85, 'Chemistry':75, 'English':83, 'History':88, 'Economy':65, 'Geography':55},
                       2:{'Math':63, 'Physics':73, 'Biology':58, 'Chemistry':45, 'English':80, 'History':68, 'Economy':75, 'Geography':85},
                       3:{'Math':84, 'Physics':85, 'Biology':82, 'Chemistry':85, 'English':60, 'History':88, 'Economy':82, 'Geography':63}}
    
        top_grades_dict = {1:{'Math':93, 'Biology':85, 'English':83, 'History':88},
                       2:{'Physics':73, 'English':80, 'Economy':75, 'Geography':85},
                       3:{'Math':84, 'Physics':85, 'Chemistry':85, 'History':88}}
    
        is_sucess = {1:1,
                     2:1,
                     3:1}
    
    The average of student 1,2,3 are 76.75, 68.375, 78.625 respectively and the standard deviation are 12.924, 12.920, 9.893, 
    The average minus standard deviation of student 1,2,3 are 63.826, 55.455, 68.732
    
        above_average_dict = {1:{'Math':93, 'Physics':70, 'Biology':85, 'Chemistry':75, 'English':83, 'History':88, 'Economy':65},
                              2:{'Math':63, 'Physics':73, 'Biology':58, 'English':80, 'History':68, 'Economy':75, 'Geography':85},
                              3:{'Math':84, 'Physics':85, 'Biology':82, 'Chemistry':85, 'History':88, 'Economy':82}}

    """
    # Create empty dictionaries to store the top 4 grades and mean - variance for each student
    grades_dict={} 
    top_grades_dict = {}
    #lower_boundary_dict = {}
    above_average_dict = {}
    # check if the student has suceeded or not
    is_sucess={}
    # Iterate through each row (student) in the dataframe
    for index, row in df.iterrows():
    # considered that the sucess average is 60/100 per course or sum grades greater than 480.    
        is_sucess[index]="1" if sum(row) >=480 else "0"
        
        # Calculate the top 4 grades for the student
        grade_dict = {column: grade for column, grade in row.items()}
        top_4_grades = dict(sorted(grade_dict.items(), key=lambda x: x[1], reverse=True)[:4])
        
        # Calculate the mean and variance for the student's grades
        mean = row.mean()
        variance = row.var()
        
        # Add the student's name (index) and their top 4 grades with column names to the top_grades_dict
        top_grades_dict[index] = top_4_grades
        
        #define the lower boundary of grades, where we will select courses with grades > mean - variance
        lower_bound = mean - math.sqrt(variance)
        
        # Add the student's name (index) and mean - variance to the result_dict
     #   lower_boundary_dict[index] = lower_bound
        
        grades_dict[index]=grade_dict
        
        above_average_grades = {column.split(' ')[0]: grade for column, grade in row.items() if grade > lower_bound}
        if above_average_grades:
            above_average_dict[index] = above_average_grades
        else:
            above_average_dict[index] = {column.split(' ')[0]: grade for column, grade in row.items()}

    return grades_dict, top_grades_dict, is_sucess , above_average_dict




def filter_grades_by_threshold(top_grades_dict, threshold=80):
    """
    For a student, Pick only the courses with grades that are larger than a threshold
    
    Parameters
    ----------
    top_grades_dict: dict 
        dictionary of course:grade 
    
    threshold: int 
        set a grade threshold value for filtering the courses on, default = 80 
    
    
    Returns
    -------
    filtered_grades_dict: dict 
        return the grades that are above threshold
    
    Examples
    --------
    Input:
        top_grades_dict = {1:{'Math':93, 'Biology':85, 'English':83, 'History':88},
                       2:{'Physics':73, 'English':80, 'Economy':75, 'Geography':85},
                       3:{'Math':84, 'Physics':85, 'Chemistry':85, 'History':88}}
    Output:
        filtered_grades_dict = {1:{'Math':93, 'Biology':85, 'English':83, 'History':88},
                                2:{'English':80, 'Geography':85},
                                3:{'Math':84, 'Physics':85, 'Chemistry':85, 'History':88}}
        
    """
    filtered_grades_dict = {}
    passing_grade_dict = {}
    for student, grades in top_grades_dict.items():
        filtered_grades = {column.split(' ')[0]: grade for column, grade in grades.items() if grade > threshold}
        passing_grade_dict = {column.split(' ')[0]: grade for column, grade in grades.items() if grade >= 60}
        if filtered_grades:
            filtered_grades_dict[student] = filtered_grades
        elif passing_grade_dict:
            filtered_grades_dict[student] = passing_grade_dict
        else:
            filtered_grades = {column.split(' ')[0]: grade for column, grade in grades.items()}
    
    return filtered_grades_dict




def combine_keys_and_calculate_average(filtered_grades_dict):
    """
    For the courses that are larger than the threshold, combine the keys (courses), and values as averages to reach out for fields that require skills on more than one course.
    
    Parameters
    ----------
    filtered_grades_dict: dict 
        dictionary of grades that are above threshold

    Returns
    -------
    combine_dict: dict 
        append the dictionary of the courses: grades found in filtered_grades_dict, by combining keys by 2 as keys and average of grades as value 
        
    Examples
    --------
    Input:
        filtered_grades_dict = {1:{'Math':93, 'Biology':85, 'English':83, 'History':88},
                                2:{'English':80, 'Geography':85},
                                3:{'Math':84, 'Physics':85, 'Chemistry':85, 'History':88}}
    Output:
        combine_dict = {1: {'Math': 93,
                            'Biology': 85,
                            'English': 83,
                            'History': 88,
                            'Math_History': 90.5,
                            'Math_English': 88.0,
                            'Math_Biology': 89.0,
                            'History_English': 85.5,
                            'History_Biology': 86.5,
                            'English_Biology': 84.0},
                        2: {'English': 80, 'Geography': 85, 'Geography_English': 82.5},
                        3: {'Math': 84,
                            'Physics': 85,
                            'Chemistry': 85,
                            'History': 88,
                            'Physics_Math': 84.5,
                            'Physics_History': 86.5,
                            'Physics_Chemistry': 85.0,
                            'Math_History': 86.0,
                            'Math_Chemistry': 84.5,
                            'History_Chemistry': 86.5}}
    
    """
    combine_dict = {}

    for student, grades in filtered_grades_dict.items():
        sorted_keys = sorted(grades.keys(), reverse=True)
        combined_grades = dict(grades)  # Create a copy of the original grades

        for i in range(len(sorted_keys)):
            for j in range(i + 1, len(sorted_keys)):
                key1 = sorted_keys[i]
                key2 = sorted_keys[j]
                combined_key = f"{key1}_{key2}"
                average_value = (grades[key1] + grades[key2]) / 2.0
                combined_grades[combined_key] = average_value

        combine_dict[student] = combined_grades

    return combine_dict


def calculate_key_probabilities(result_dict):
    """
    Takes the dictionary resulting from combine_keys_and_calculate_average and calculate the probability of each key defined by the formula: value/sum(values)
    
    Parameters
    ----------
    result_dict: dict
        Takes the dictionary resulting from combine_keys_and_calculate_average
    
    Returns
    -------
    key_probabilities_dict: dict
        Return a dictionary having courses obtained from result_dict as keys and value/sum of values as values    
    
    Examples
    --------
    Input:
        result_dict = {1: {'Math': 93,
                            'Biology': 85,
                            'English': 83,
                            'History': 88,
                            'Math_History': 90.5,
                            'Math_English': 88.0,
                            'Math_Biology': 89.0,
                            'History_English': 85.5,
                            'History_Biology': 86.5,
                            'English_Biology': 84.0},
                        2: {'English': 80, 'Geography': 85, 'Geography_English': 82.5},
                        3: {'Math': 84,
                            'Physics': 85,
                            'Chemistry': 85,
                            'History': 88,
                            'Physics_Math': 84.5,
                            'Physics_History': 86.5,
                            'Physics_Chemistry': 85.0,
                            'Math_History': 86.0,
                            'Math_Chemistry': 84.5,
                            'History_Chemistry': 86.5}}        
    Output:
        key_probabilities_dict = {1: {'Math': 0.10659025787965616,
                                      'Biology': 0.09742120343839542,
                                      'English': 0.09512893982808023,
                                      'History': 0.1008595988538682,
                                      'Math_History': 0.10372492836676218,
                                      'Math_English': 0.1008595988538682,
                                      'Math_Biology': 0.10200573065902578,
                                      'History_English': 0.09799426934097422,
                                      'History_Biology': 0.0991404011461318,
                                      'English_Biology': 0.09627507163323783},
                                  2: {'English': 0.32323232323232326,
                                      'Geography': 0.3434343434343434,
                                      'Geography_English': 0.3333333333333333},
                                  3: {'Math': 0.09824561403508772,
                                      'Physics': 0.09941520467836257,
                                      'Chemistry': 0.09941520467836257,
                                      'History': 0.10292397660818714,
                                      'Physics_Math': 0.09883040935672514,
                                      'Physics_History': 0.10116959064327485,
                                      'Physics_Chemistry': 0.09941520467836257,
                                      'Math_History': 0.10058479532163743,
                                      'Math_Chemistry': 0.09883040935672514,
                                      'History_Chemistry': 0.10116959064327485}}
    """
    key_probabilities_dict = {}

    # Initialize a dictionary to store the sum of values for each key
    key_sums = {}

    # Initialize a dictionary to store student numbers and their corresponding sums
    student_sums = {}

    # Iterate through each student's grades in result_dict
    for student, grades in result_dict.items():
        student_sum = 0
        for key, value in grades.items():
            # Initialize the sum for the key if it doesn't exist
            key_sums.setdefault(key, 0)
            key_sums[key] += value
            student_sum += value  # Sum for the current student
        student_sums[student] = student_sum  # Store the student's sum

    # Calculate the sum of all values across all keys
    total_sum = sum(key_sums.values())

    # Calculate the probabilities for each key and include the student number
    for student, grades in result_dict.items():
        student_key_probabilities = {}
        for key, value in grades.items():
            probability = value / student_sums[student]
            student_key_probabilities[key] = probability
        key_probabilities_dict[student] = student_key_probabilities

    return key_probabilities_dict




def draw_values_with_weights(key_probabilities, value_lists):
    """
    Draw a major, from value_lists of majors, taking into account the weight that was calculated in the key_probabilities_dict
    
    Parameters
    ----------
    key_probabilities: dict 
        A dictionary with keys as courses and their combintations and values as weights between 0 and 1
        
    value_lists: dict 
        A dictionary having the courses as keys and majors (fields) as values
        
    Returns
    -------
    drawn_values: dict 
        Returns the major that was drawn
      
    """
    drawn_values = {}
    
    for student, probabilities in key_probabilities.items():
        student_drawn_values = {}
        value_list = []
        weights=[]
        for key, probability in probabilities.items():
            # Get the list of values based on the key
            value_list.append(value_lists[key])
            weights.append(probability)
            
            # Use random.choices to draw one value based on the probability
            if value_list:  # Check if the value_list is not empty
                drawn_value = random.choices(random.choices(value_list, weights=weights, k=1)[0])
            else:
                drawn_value = None
            
            #student_drawn_values[key] = drawn_value

        drawn_values[student] = drawn_value #student_drawn_values

    return drawn_values






def create_suggestion_string_column(df,dict):
    """The function would create a column with col_name in a dataframe df from a dictionary dict, 
    if `is_sucess` == 0, the value of the row in a column will be Fail
    otherwise, concatenates elemetns of a list (or iterable) into a single string
    
    Parameters
    ----------
    df: DataFrame
        The DataFrame where the column is to be created
        
    dict: dict
        
    
    Returns
    -------
    column: 
        a column
    
    """
    df["default"] = dict
    df["default"]=np.where(df['is_sucess'] == '1', df["default"], 'Fail')
    df["default"] = np.where(df["default"] != 'Fail', df["default"].apply(", ".join), 'Fail')
    
    return df["default"]