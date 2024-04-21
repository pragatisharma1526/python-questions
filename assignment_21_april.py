#PANDAS
'''2. Group the sales data by product category and customer segment, and
calculate the total sales and average discount for each group. Submit
the grouped and aggregated DataFrame.'''

import pandas as pd
df=pd.read_csv("sales_data.csv")


grouped_sales_data=df.groupby(['product_category','customer_segment']).agg({'sales':'sum','discount':'mean'
}).reset_index()

print(grouped_sales_data)



'''3. Merge the sales data with a separate product details DataFrame (you
can create a dummy product details DataFrame) based on the product
ID. Submit the merged DataFrame.'''
import pandas as pd
df=pd.read_csv("sales_data.csv")

product_detail=pd.DataFrame({
    "product_name":['product A','product B','product C'],
    "product_category":['category A','category B','category C']})
merge_data=pd.merge(sales_data,product_detail,on=('product_category'))
print(merge_data)

'''1
Load the "sales_data.csv" dataset and handle any missing data using
appropriate techniques (e.g., dropping rows/columns, imputation).
Submit the cleaned DataFrame.'''
import pandas as pd
df=pd.read_csv("sales_data.csv")
missing_data=df.isnull().sum()
print(missing_data)
cleaned_data=df.dropna()






#NUMPY
'''Compute the correlation matrix for the numerical features of the iris
dataset using NumPy's linear algebra functions. Submit the correlation
matrix and your code.'''
import numpy as np

iris_data=pd.read_csv("Iris.csv")
numerical_features=iris_data.drop(columns=['Species'])

correlation_matrix=np.corrcoef(numerical_features,rowvar="FALSE")
print(correlation_matrix)



#EXCEL
'''4. Discuss the advantages and limitations of using Excel for data analysis,
and when it might be more appropriate to use other tools or
programming languages.'''
#USER-FRIENDLY INTERFAce
#Built-in functions and formulas
#Quick Prototyping

#LIMITATIONS
#Data Integrity and Security
#Limited Capacity
#Limited Automation
