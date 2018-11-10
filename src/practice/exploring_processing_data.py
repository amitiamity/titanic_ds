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
print(df.tail())


