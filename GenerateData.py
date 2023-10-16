import pandas as pd
import random
import numpy as np

from scipy.cluster.vq import kmeans, vq, whiten
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import combinations
import re
import math

#Threshold of split
threshold = 80

#number of sample to be generated
nsample = 1000000

#list of fields:
Math_Geography = ["Surveying and Geomatics", "Geographic Information Systems", "Cartography", "Metorology"]
Math_Economy = ["Economics", "Financial Services", "Risk Manager","Quantitative Analyst"]
Math_Chemistry =["Chemical Engineering","Medicinal Chemistry","Analytical Chemistry","Quantum Chemistry","Chemical Education","Computational Chemistry"]
Math_Biology =["Bioinformatics","Epidemiology","Biostatistics","Computational Biology","Mathematical Biology"]
Math_History =["Actuarial Science","Economic History Research","Mathematical Archaeology","Quantitative Historical Analysis","Statistical Demography"]
Math_English = ["Technical Writing","Data Reporting", "Math Journalism"]
Math=["Mathematics","Data Analysis","Data Scientist","Computer Science","Signal Processing Engineers","Operation Resarch"]


Physics_Math =["Mathematical Modeling","Quantum Mechanics","Mathematical Physics"]
Physics_Chemistry =["Materials Science","Chemical Engineering","Environmental Chemistry","Physical Chemistry","Geochemistry","Atmospheric Chemistry"]
Physics_Biology =["Biophysics","Biomedical Engineering","BioMechanics","Medical Physics","Physiology","Radiology"]
Physics_History =["History of Physics","Philosophy of Physics","Science Education and Outreach","Historical Instrumentation and Experimental Replication","Science Communication and Writing","Historical Analysis of Technological Advances"]
Physics_English =["Science Writing","Technical Writing in Physics","Physics Journalism","Physics Education","Science Communication","Publishing and Editing in Physics","Research in Science and Technology Communication","Physics Content Creation","Science Editing","Curriculum Development"]
Physics_Economy=["Energy Economics", "econophysics"]
Physics_Geography = ["Geospatial Techoology","Plantery Science", "GeoPhysics", "Climate Science"]
Physics =["Theortical Physics","Astrophysics","Experimental Physics","Physics Education","Science Journalism"]


Chemistry_Biology =["Biochemistry","Pharmacology","Molecular Biology"]
Chemistry=["Analytical Chemistry","Organic Chemistry","Education","Inorganic Chemistry","Lab Assistant"]

Biology =["Biotechnology","Microbiology","Anatomy","Ecology","Medicine"]



History_English =["Historical Research and Writing","Archival Studies","Digital Humanities","Historiography and Criticism","Historical Journalism","Museum Curation and Interpretation","Historical Fiction Writing","Cultural Heritage Preservation","Academic Publishing","Historical Education and Outreach"]
History_Biology =["History of Science","Environmental History","Medical History","Historical Anthropology","Museum Curator","Bioarchaeology"]
History_Chemistry=["Chemistry and Scientific Revolution", "History of Chemical Discoveries", "Evolution of Chemical Education"]
History_Economy =["Economic History","Economic Policy Analysis","Financial Sector Regulatoins","Business and Economic Journalism"]
History =["Museum Curator","Archivist","Journalism and Media","Government and Public Services","Historical Preservation and Cultural Heritage"]



English_Biology =["Journalism","Public Relations","Copywriting","Publishing","Editing","Technical Writing","Education","Content Management","Digital Marketing","Creative Writing"]
English_Chemistry = ["Scientific Writing in Chemistry", "Chemistry Journalism", "Technical Writing for Chemistry", "Chemistry Education and Curriculum Development"]
English_Economy = ["Global Financial Markets","English Language Skills for Economic Forecasting"]
English =["Writing and Editing","Journalism","Public Relations","Copywriting","Content Creation","Publishing","Technical Writing","Education","Translation","Communications"]

Economy_Chemistry = ["Sustainable Chemistry and Economic Development", "Chemical Supply Chain Management", "Economics of Chemical Manufacturing", "Chemical Market Forecasting and Analysis", "Chemistry and Resource Economics", "Cost-benefit Analysis in Chemical Projects", "Economic Policies in the Chemical Sector"]
Economy_Biology = ["Biotechnology and Economic Development", "Economics of Biomedical Research and Development", "Sustainable Economics in Biology Conservation"]
Economy =["Microeconomics","Macroeconomics","Economic Policy","International Economics","Public Finance","Econometrics"]

Geography_Biology = ["Landscape Ecology and Biotic Interactions","Conservation of Biodiversity Hotspots","Geographical Perspectives on Ecosystem Services"]
Geography_Chemistry=["Geography of Chemical Waste Management", "Spatial Dynamics of Chemical Reactions"]
History_Geography =["Historical Geography","Cultural Heritage Management and Preservation","Archaeology","Academic Research and Teaching"]
Geography_English =["Academic Research","Travel Writing and Guidebook Publishing","Environmental Jouralism","Cultural Heritage Preservation"]
Geography_Economy =["International Development","Environmental Economics","Urban Planing and Regional Development"]
Geography =["Transportation and Logistics","Emergency management and Disaster","Tourism and Hospitality"]


value_lists = {'Math_Geography': Math_Geography,
               'Math_Economy': Math_Economy,
               'Math_Chemistry': Math_Chemistry,
               'Math_Biology': Math_Biology,
               'Math_History': Math_History,
			   'Math_English':Math_English,
               'Math': Math,
               'Physics_Math': Physics_Math,
               'Physics_Chemistry': Physics_Chemistry,
               'Physics_Biology': Physics_Biology,
               'Physics_History': Physics_History,
               'Physics_English': Physics_English,
			   'Physics_Economy': Physics_Economy,
			   'Physics_Geography':Physics_Geography,
               'Physics':Physics,
               'Chemistry_Biology':Chemistry_Biology,
			   'History_Chemistry':History_Chemistry,
               'Chemistry': Chemistry,
               'Biology':Biology,
               'History_English':History_English,
               'History_Biology':History_Biology,
               'History_Economy':History_Economy,
               'History':History,
               'English_Biology':English_Biology,
               'English_Chemistry':English_Chemistry,
			   'English_Economy':English_Economy,
			   'English':English,
			   'Economy_Chemistry':Economy_Chemistry,
			   'Economy_Biology':Economy_Biology,
               'Economy':Economy,
               'History_Geography':History_Geography,
			   'Geography_Biology':Geography_Biology,
			   'Geography_Chemistry':Geography_Chemistry,
               'Geography_English':Geography_English,
               'Geography_Economy':Geography_Economy,
               'Geography':Geography
               }

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



# Code 

df=generate_Grades(nsample)
top_grades_dict, new_mean, is_success, above_average_grade = process_student_grades(df)


#first method:  Take the top 4 grades, then filter the grades in top 4 grades to those larger than threshold =  80. if the top 4 grades are all below 80 then take the grades that are larger than 60
top_grades_dict_above_80 = filter_grades_by_threshold(top_grades_dict, threshold)
# combine the courses by two ordered by Z to A by course name separated by _
combined_majors = combine_keys_and_calculate_average(top_grades_dict_above_80)
# calulate a weight for each course and it's combination based on the grade / sum of grades
combined_majors_probability = calculate_key_probabilities(combined_majors)
# from the list of lists pick a field and suggest it taking into account the weight from where the field to be drawn from
suggested_field = draw_values_with_weights(combined_majors_probability, value_lists)



# add the is_sucess dictionary as a column to df as it would be either to fiter for the student that passed
df['is_sucess']=is_success
#df['is_sucess']=df['is_sucess'].astype(bool)

# add the suggested_field as a column and then create a new column that takes the value of suggested field if is_sucess =1 otherwise print fail
df['Suggestion Based on Top 4 grades'] = create_suggestion_string_column(df,suggested_field)





#second method: The second method is based on picking the courses that are above the mean-sqrt(var) of each student instead of gettting the top 4 grades and then filtering for threshold = 80 then 60
# from the process_student_grade, we had the above_average_dict

combined_majors_2= combine_keys_and_calculate_average(above_average_grade)
combined_majors_probability_2 = calculate_key_probabilities(combined_majors_2)
suggested_field_2 = draw_values_with_weights(combined_majors_probability_2, value_lists)
df['Suggestion Based on Mean'] = create_suggestion_string_column(df,suggested_field_2)


df.drop('default',axis=1, inplace = True)
df.to_csv(f'Generated_data_{nsample}.csv', index=False)


#plotting distribution by role:
plotPerColumnDistribution(df, 'Suggestion Based on Top 4 grades')
plotPerColumnDistribution(df, 'Suggestion Based on Mean')



#df.to_csv('c:/Users/eljawadmo/OneDrive - City of Ottawa/Documents/Workspace/PowerBi/Power BI Demo/University RecommendationsToBeClustered.csv', index=False)

# Prepare the feature data for clustering (excluding any non-numeric columns and the student id, if present)
features  = df.drop('Student ID',axis =1)
features = features.astype(float) 
scaled_features = whiten(features)





#
distortions = []
num_clusters = range(1,100)
for i in num_clusters:
    cluster_centers, distortion = kmeans(scaled_features,i)
    distortions.append(distortion)
    
# Create a DataFrame with two lists - num_clusters, distortions
elbow_plot = pd.DataFrame({'num_clusters': num_clusters, 'distortions': distortions})


# Creat a line plot of num_clusters and distortions
sns.lineplot(x='num_clusters', y='distortions', data = elbow_plot)
plt.xticks(num_clusters)
plt.show()