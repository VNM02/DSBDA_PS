# -*- coding: utf-8 -*-
"""PS11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_qctjRppHNGYH2hdnr1gVoQj2F4tZHXm
"""

import pandas as pd

data=pd.read_csv('movies_metadata.csv',engine='python', error_bad_lines=False)
print(data)

data.describe()

print(data.dtypes)

null_values = data.isnull().sum()
print(null_values)

data.dropna(inplace=True)
print(data)

print("Rows : = "+str(data.shape[0]))
print("Cols : = "+str(data.shape[1]))

print(data['original_language'])

unique_vals=data['original_language'].unique()
print(unique_vals)

en_lang = data[data['original_language'] == 'en']
print(en_lang)

hi_lang = data[data['original_language'] == 'hi']
print(hi_lang)

ja_lang = data[data['original_language'] == 'ja']
print(ja_lang)

merged_subset=pd.concat([en_lang,ja_lang])
print(merged_subset)

rating_data=pd.read_csv('ratings_small.csv');
data.rename(columns={'movieId': 'id'}, inplace=True)
print(rating_data)

print(data['id'])

data['id'] = data['id'].astype(int)

merged_df = pd.merge(data, rating_data, left_on='id', right_on='movieId', how='inner')
print(merged_df)

sorted_data=merged_df.sort_values(by='rating')
print(sorted_data)

print(sorted_data.head(10))   # To show first 10 records

transposed_data = data.transpose()
print(transposed_data)

melted_data = pd.melt(data, id_vars=['original_language', 'id'], var_name='Metric', value_name='Value')
print(melted_data)

wide_data = melted_data.pivot_table(index=['id'], columns='Metric', values='Value')
print(wide_data)