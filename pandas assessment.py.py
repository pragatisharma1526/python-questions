import pandas as pd
import numpy as np

# Creating a dummy dataset
data = {
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
'Age': [25, 30, 35, 40, 45],
'Salary': [50000, 60000, 70000, 80000, 90000],
'Department': ['HR', 'IT', 'Finance', 'HR', 'IT'],
'Start_Date': pd.to_datetime(['2020-01-01', '2019-03-15', '2021-05-20', '2018-09-10', '2022-02-28']),
'Experience': [5, 10, 3, 15, 2],
'Rating': [4.2, 3.8, 4.5, 4.0, 4.7]
}

df=pd.DataFrame(data)
print(df)

# question 1:
# Select employees older than 30
older_than_30 = df[df['Age'] > 30]
print(older_than_30)

#Question 3: Calculating Summary Statistics
#Let's calculate summary statistics for the numerical columns in the DataFrame:
summary_stats=df[['Name','Age','Salary','Department','Start_Date','Experience','Rating']].describe()
print(summary_stats)



#Question 4: Reshaping the Layout of Tables
#Let's reshape the DataFrame to have "Name" as the index and "Department" as columns, with"Salary" as values:
reshape_data=df.melt(id_vars=['Name','Age','Start_Date','Experience','Rating','Salary'],
                     var_name='Department',value_name="Value")
print(reshape_data)

#Question 5: Combining Data from Multiple Tables
#Let's create another DataFrame with bonus information and merge it with the originalDataFrame:
merge_data={'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'Bonus':[5000,7000,4000,100000,8000]}
merge_data1=pd.DataFrame(merge_data)
print(merge_data1)
merge_data2=pd.merge(df,merge_data1,on='Name')
print(merge_data2)



# question 6:
 #Manipulating Textual Data
#Let's create a new column based on the length of the employee's name:
df['New_col'] = df['Name'].apply(lambda x: len(x))
print(df)

#Question 7: Filtering Data Based on Multiple Conditions
#Let's filter the DataFrame to include only employees from the IT department who are older than 30:
filter_data = df[(df['Department'] == 'IT') & (df['Age'] > 30)]
print(filter_data)




#Question 8: Creating a New Column Based on Conditions
#Let's create a new column called "Performance" based on the employee's rating:
def categorize_performance(rating):
    if rating >= 4.5:
        return 'Excellent'
    elif rating >= 4.0:
        return 'Good'
    else:
        return 'Average'

df['Performance'] = df['Rating'].apply(categorize_performance)
print(df)

#Question 9: Calculating Group-Wise Summary Statistics
#Let's calculate the mean salary and experience for each department:
department_summary = df.groupby('Department').agg({'Salary': 'mean', 'Experience': 'mean'})
print(department_summary)

#Question 10: Sorting Data
#Let's sort the DataFrame by age in descending order:
df_sorted = df.sort_values(by='Age', ascending=False)
print(df_sorted)

#Question 11: Concatenating DataFrames
#Let's create a new DataFrame with additional employee information and concatenate it with the original DataFrame:
new_data = {
    'Name': ['Pragati', 'Aniya', 'Priyanshi'],
    'Age': [38, 28, 39],
    'Salary': [72000, 65000, 85000],
    'Department': ['HR', 'Finance', 'IT'],
    'Start_Date': pd.to_datetime(['2019-07-15', '2020-11-30', '2023-04-12']),
    'Experience': [8, 5, 12],
    'Rating': [4.3, 4.1, 4.6]
}
new_df = pd.DataFrame(new_data)


concatenated_df = pd.concat([df, new_df], ignore_index=True)
print(concatenated_df)







