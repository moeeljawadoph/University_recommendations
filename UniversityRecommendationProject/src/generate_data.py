# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 00:35:58 2023

@author: eljawadmo

This file contains the code to be run when generating data
"""

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