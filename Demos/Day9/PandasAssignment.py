
'''
Use following data to answer the questions: Sample Python dictionary data and list labels:

exam_data = {'name': ['Sonu', 'Raja', 'Ketaki', 'Rupa', 'Radha', 'Reshma', 'Keshav', 'Narendra', 'Rani', 'Kittu"],'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19),'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 11,'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'])

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 7, 7]



'''
import numpy as np
import pandas as pd
exam_data = {'name': ['Sonu', 'Raja', 'Ketaki', 'Rupa', 'Radha', 'Reshma', 'Keshav', 'Narendra', 'Rani', 'Kittu'],'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 11],'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 7, 7]
df=pd.DataFrame(exam_data)
print(df) 

#1. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index 
#labels (a,b,c,d,e.....).
df1=pd.DataFrame(exam_data,index=labels)
print(df1) 

#2. Write a Pandas program to display a summary of the basic information about a specified Dataframe and its data.

df1.info()

#3. Write a Pandas program to get the first 3 rows of a given DataFrame
df1.head(3)
df1.iloc[0:3]
df1.loc['a':'c']

#4. Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
df1[['name','score']]


#5. Write a Pandas program to rename columns of a given DataFrame(only for q5 use below data).

d={'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df5=pd.DataFrame(d)

df5.rename(columns={"col1":'col5'})

#6. Write a Pandas program to select the specified columns and rows from a given DataFrame. 
#Select 'name' and 'score' columns in rows 1, 3, 5, 7 from the following data frame.

df1.loc[['a','c','f','h'],['name','score']]

#7. Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.
df1[df1['attempts']>2]

#8. Write a Pandas program to count the number of rows and columns of a DataFrame.

df1.shape
df1.shape[0]

#9. Write a Pandas program to select the rows where the score is missing, i.e. is NaN.
df1[df1['score'].isna()]

# 10. Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).
df1[(df1['score']>=15)  & (df1['score'] <=20)]

#11. Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score
# greater than 15.

df1[(df1['attempts']<=2)  & (df1['score'] >=15)]

#12. Write a Pandas program to calculate the sum of the examination attempts by the students.
df1['attempts'].sum()

#13. Write a Pandas program to calculate the mean score for each different student in data frame.
df1['score'].mean()
df1.groupby('name')['score'].mean()

#14. Write a Pandas program to append a new row 'k' to DataFrame with given values for each column. Now delete the new row
#and return the original data frame.
df1.loc['k']=['akshay',25,1,'yes']
print(df1)

df1.drop('k',axis=0,inplace=True)
df1

#15. Write a Pandas program to sort the data frame first by 'name' in descending order, then by 'score' in 
#ascending order.
df1.sort_values(['name','score'],ascending=[True,False])

#16. Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False

df['qualify'].map({'yes': True, 'no': False})

#17. Write a Pandas program to delete the 'attempts' column from the DataFrame.
df1.pop('attempts')
df1

#18. Write a Pandas program to insert a new column in existing DataFrame.
df1['new']=10
df1

