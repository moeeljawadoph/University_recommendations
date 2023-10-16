# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 00:25:20 2023

@author: eljawadmo

The file contains all the custom functions created in this project
"""


def generate_Grades(n_samples):
    """
    Generate n_samples rows with courses as columns and students as rows.
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




def filter_grades_by_threshold(top_grades_dict, threshold):
    """
    Pick only the courses from grades that are larger than a threshold, that is calculated for each student alone
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
    for the courses that are larger than the threshold, combine the keys (courses), and values as averages to reach out for fields that require skills on more than one course.
    
    For example:
        
    
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




# Distribution graphs (histogram/bar graph) of column data
def plotPerColumnDistribution(df, column_name,nbins=None):
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


def create_suggestion_string_column(df,dict):
    """The function would create a column with col_name in a dataframe df from a dictionary"""
    df["default"] = dict
    df["default"]=np.where(df['is_sucess'] == '1', df["default"], 'Fail')
    df["default"] = df["default"].apply(", ".join)
    return df["default"]