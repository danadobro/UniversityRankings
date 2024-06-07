#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 00:15:26 2024

@author: danadobrosavljevic
"""

import pandas as pd
import json

json_file = open('top_100_universities_2023.json')
json_file2 = open('top_100_universities_2024.json')


data1 = json.load(json_file)
data2 = json.load(json_file2)



#storing json data in a data frame
data_2023 = pd.DataFrame(data1)
data_2024 = pd.DataFrame(data2)


data_2023.describe()
data_2024.describe()



#check the numbers
is_rank_numeric = pd.api.types.is_numeric_dtype(data_2024['rank'])
is_number_of_students_numeric = pd.api.types.is_numeric_dtype(data_2024['number_of_students'])



data_2023.describe()
data_2023.info()


#change to numeric
data_2023['rank'] = data_2023['rank'].str.replace('=', '')
data_2023['rank'] = pd.to_numeric(data_2023['rank'], errors='coerce')
data_2023['number_of_students'] = data_2023['number_of_students'].str.replace(',', '')
data_2023['number_of_students'] = pd.to_numeric(data_2023['number_of_students'], errors='coerce')
data_2023['student_per_staff'] = pd.to_numeric(data_2023['student_per_staff'], errors='coerce')


data_2023['intl_students_percentage'] = data_2023['intl_students_percentage'].str.replace('%', '')
data_2023['intl_students_percentage'] = pd.to_numeric(data_2023['intl_students_percentage'], errors='coerce')


#making 2 columns out of female_male_ratio
data_2023[['female_ratio', 'male_ratio']] = data_2023['female_male_ratio'].str.split(' : ', expand=True)


data_2023['female_ratio'] = pd.to_numeric(data_2023['female_ratio'], errors='coerce')
data_2023['male_ratio'] = pd.to_numeric(data_2023['male_ratio'], errors='coerce')


data_2023['year'] = 2023
data_2023['year'] = pd.to_datetime('2023-01-01')


#changing strings to numerical values for 2024 data

data_2024.describe()
data_2024.info()

#change to numeric
data_2024['rank'] = data_2024['rank'].str.replace('=', '')
data_2024['rank'] = pd.to_numeric(data_2024['rank'], errors='coerce')
data_2024['number_of_students'] = data_2024['number_of_students'].str.replace(',', '')
data_2024['number_of_students'] = pd.to_numeric(data_2024['number_of_students'], errors='coerce')
data_2024['student_per_staff'] = pd.to_numeric(data_2024['student_per_staff'], errors='coerce')


data_2024['intl_students_percentage'] = data_2024['intl_students_percentage'].str.replace('%', '')
data_2024['intl_students_percentage'] = pd.to_numeric(data_2024['intl_students_percentage'], errors='coerce')


#making 2 columns out of female_male_ratio
data_2024[['female_ratio', 'male_ratio']] = data_2024['female_male_ratio'].str.split(' : ', expand=True)


data_2024['female_ratio'] = pd.to_numeric(data_2024['female_ratio'], errors='coerce')
data_2024['male_ratio'] = pd.to_numeric(data_2024['male_ratio'], errors='coerce')



data_2024['year'] = 2024
data_2024['year'] = pd.to_datetime('2024-01-01')


data_2023.to_csv('top_100_universities_2023_cleaned.csv', index= True)
data_2024.to_csv('top_100_universities_2024_cleaned.csv', index= True)


all_rankings = pd.merge(data_2023, data_2024, on='name', how='outer', suffixes=('_2023', '_2024'))
all_rankings.to_csv('all_rankings.csv', index= True)