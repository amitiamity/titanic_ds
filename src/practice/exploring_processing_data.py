import numpy as np;
import pandas as pd;
import os

raw_data_path = os.path.join(os.path.pardir,'data','raw')
train_file_path = os.path.join(raw_data_path,'train.csv')
test_file_path = os.path.join(raw_data_path,'test.csv')
#read data as dataframe
train_df = pd.read_csv(train_file_path,index_col='PassengerId')
test_df = pd.read_csv(test_file_path,index_col='PassengerId')
#print(train_df.info())
#print(test_df.info())

#we need to predict the survived possibility value for passenger in test dataset.
#Let's create the Survived column in test df with dummy value -888
test_df['Survived'] = -888
# print(test_df.info())
#concat the test and train data
df = pd.concat((train_df,test_df),axis=0)
#axis = 0, append the data of second df into first one
#axis = 1, append the second df next to the first df columns, default is axis  = 0
# print(df.info())
# print(df.tail())

#selection, indexes, filtering using pandas
#1. selecting specific columns
# print(df.Name)
# print(df['Name'])
#2. multiple cols
# print(df[['Name','Age']])
#3. label based indexing #all columns, fetch rows between 5 to 10
# print(df.loc[5:10,])

#4 selecting column range
# print(df.loc[5:10,'Age':'Ticket'])
#5 selecting discrete columns
print(df.loc[5:10,['Age','Ticket']])

#position based indexing
print(df.info())
print(df.iloc[5:10,3:5])

#filtering data
print(df.loc[df.Sex == 'male',['Age']])
#all columns and rows where Sex is male
print(df.loc[df.Sex== 'male',:])
#use & and or operator
print(df.loc[((df.Sex == 'male') & (df.Pclass == 1)),:])

#Summary Statistics


