# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:17:48 2024

@author: KEKAELK1
"""

import pandas as pd

# Load the dataset
file_path = "movie_dataset.csv"  
movie_data = pd.read_csv(file_path)

# Replace spaces in column names with underscores
movie_data.columns = movie_data.columns.str.replace(' ', '_')

# Check for missing values
missing_values = movie_data.isnull().sum()

# Replace missing values with column averages
for column in movie_data.columns:
    if movie_data[column].dtype == 'float64':
        mean_value = movie_data[column].mean()
        movie_data[column].fillna(mean_value, inplace=True)

# Save the cleaned dataset to a new CSV file
cleaned_file_path = "C:/Users/kekaelk1/css2024_project1/cleaned_movie_dataset.csv"  # Replace with the desired file path
movie_data.to_csv(cleaned_file_path, index=False)

# Display the cleaned dataset
print(movie_data.head())


#question 1

import pandas as pd

# Load the cleaned dataset
cleaned_file_path = "cleaned_movie_dataset.csv" 
cleaned_movie_data = pd.read_csv(cleaned_file_path)

# Find the row with the highest rating
highest_rated_movie = cleaned_movie_data.loc[cleaned_movie_data['Rating'].idxmax()]

# Display the highest-rated movie
print("The highest-rated movie in the dataset is:")
print(highest_rated_movie[['Title', 'Rating']])


#question 2

import pandas as pd

# Load the cleaned dataset
cleaned_file_path = "cleaned_movie_dataset.csv"  
cleaned_movie_data = pd.read_csv(cleaned_file_path)

# Calculate the average revenue
average_revenue = cleaned_movie_data['Revenue_(Millions)'].mean()

print(f"The average revenue of all movies in the dataset is: {average_revenue} Million")


#question 3

import pandas as pd

# Load the cleaned dataset
cleaned_file_path = "cleaned_movie_dataset.csv"  
cleaned_movie_data = pd.read_csv(cleaned_file_path)

# Filter movies from 2015 to 2017
filtered_movies = cleaned_movie_data[(cleaned_movie_data['Year'] >= 2015) & (cleaned_movie_data['Year'] <= 2017)]

# Calculate the average revenue for the filtered movies
average_revenue_2015_to_2017 = filtered_movies['Revenue_(Millions)'].mean()

print(f"The average revenue of movies from 2015 to 2017 in the dataset is: {average_revenue_2015_to_2017} Million")


#question 4

import pandas as pd

# Load the cleaned dataset
cleaned_file_path = "cleaned_movie_dataset.csv" 
cleaned_movie_data = pd.read_csv(cleaned_file_path)

# Count the number of movies released in the year 2016
movies_2016_count = cleaned_movie_data[cleaned_movie_data['Year'] == 2016].shape[0]

print(f"The number of movies released in the year 2016 is: {movies_2016_count}")


# question 5

import pandas as pd

# Load the cleaned dataset
cleaned_file_path = "cleaned_movie_dataset.csv"  
cleaned_movie_data = pd.read_csv(cleaned_file_path)

# Count the number of movies directed by Christopher Nolan
nolan_movies_count = cleaned_movie_data[cleaned_movie_data['Director'] == 'Christopher Nolan'].shape[0]

print(f"The number of movies directed by Christopher Nolan is: {nolan_movies_count}")


# Question 6

import pandas as pd

# Load the cleaned dataset
cleaned_file_path = "cleaned_movie_dataset.csv"  
cleaned_movie_data = pd.read_csv(cleaned_file_path)

# Count the number of movies with a rating of at least 8.0
highly_rated_movies_count = cleaned_movie_data[cleaned_movie_data['Rating'] >= 8.0].shape[0]

print(f"The number of movies with a rating of at least 8.0 is: {highly_rated_movies_count}")


# Question 7

import pandas as pd

# Load the cleaned dataset
cleaned_file_path = "cleaned_movie_dataset.csv"  
cleaned_movie_data = pd.read_csv(cleaned_file_path)

# Filter movies directed by Christopher Nolan
nolan_movies = cleaned_movie_data[cleaned_movie_data['Director'] == 'Christopher Nolan']

# Calculate the median rating
median_rating_nolan_movies = nolan_movies['Rating'].median()

print(f"The median rating of movies directed by Christopher Nolan is: {median_rating_nolan_movies}")


# Question 8

import pandas as pd

# Load the cleaned dataset
cleaned_file_path = "cleaned_movie_dataset.csv"  
cleaned_movie_data = pd.read_csv(cleaned_file_path)

# Calculate the average rating for each year
average_rating_by_year = cleaned_movie_data.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year_highest_avg_rating = average_rating_by_year.idxmax()

print(f"The year with the highest average rating is: {year_highest_avg_rating}")


# Question 9

import pandas as pd

# Load the cleaned dataset
cleaned_file_path = "cleaned_movie_dataset.csv"  
cleaned_movie_data = pd.read_csv(cleaned_file_path)

# Count the number of movies made in 2006 and 2016
movies_2006 = cleaned_movie_data[cleaned_movie_data['Year'] == 2006].shape[0]
movies_2016 = cleaned_movie_data[cleaned_movie_data['Year'] == 2016].shape[0]

# Calculate the percentage increase
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

print(f"The percentage increase in the number of movies made between 2006 and 2016 is: {percentage_increase}%")


# Question 10

import pandas as pd
from collections import Counter

# Load the cleaned dataset
cleaned_file_path = "cleaned_movie_dataset.csv"  
cleaned_movie_data = pd.read_csv(cleaned_file_path)

# Split the multiple actors in each row and create a list of all actors
all_actors = cleaned_movie_data['Actors'].str.split(', ').explode().tolist()

# Count the occurrences of each actor
actor_counts = Counter(all_actors)

# Find the most common actor
most_common_actor = actor_counts.most_common(1)[0][0]

print(f"The most common actor in all the movies is: {most_common_actor}")


# Question 11

import pandas as pd

# Load the cleaned dataset
cleaned_file_path = "cleaned_movie_dataset.csv"  
cleaned_movie_data = pd.read_csv(cleaned_file_path)

# Split the multiple genres in each row and create a list of all genres
all_genres = cleaned_movie_data['Genre'].str.split(', ').explode().tolist()

# Count the unique genres
unique_genres_count = len(set(all_genres))

print(f"The number of unique genres in the dataset is: {unique_genres_count}")


# Question 12

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset
cleaned_file_path = "cleaned_movie_dataset.csv"  
cleaned_movie_data = pd.read_csv(cleaned_file_path)

# Select only numerical features for correlation analysis
numerical_features = cleaned_movie_data.select_dtypes(include=['float64'])

# Calculate the correlation matrix
correlation_matrix = numerical_features.corr()

# Plot the correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix of Numerical Features')
plt.show()

# Question 13

