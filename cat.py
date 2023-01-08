#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#initialising
Transformed_Housing_Data = pd.read_csv('Transformed_Housing_Data')
Transformed_Housing_Data.info()
#ID columns is useless so we are droping it
Transformed_Housing_Data.drop( columns = 'ID', inplace = True)
Transformed_Housing_Data['Condition of the House'].head(10)
Transformed_Housing_Data['Condition of the House'].value_counts()#count all unique values
#plotting some graphs
Transformed_Housing_Data.groupby('Condition of the House',
                                )['Sale Price'].mean().plot(kind = 'bar')
Transformed_Housing_Data.groupby('Condition of the House',
                                )['Sale Price'].mean().sort_values().plot(kind = 'bar')
Transformed_Housing_Data.groupby('Waterfront View',
                                )['Sale Price'].mean().sort_values().plot(kind = 'bar')
ransformed_Housing_Data.groupby('Ever Renovated',
                                )['Sale Price'].mean().sort_values().plot(kind = 'bar')
Transformed_Housing_Data.groupby('Zipcode',
                                )['Sale Price'].mean().sort_values().plot(kind = 'bar')
#creating dummies variable as categorical can't use in regression
Transformed_Housing_Data=pd.get_dummies(Transformed_Housing_Data,
                                        columns=['Condition_of_the_House','Ever_Renovated','Waterfront_View'],
                                        drop_first=True)
Transformed_Housing_Data.head(10)
#if unique value of categorical variable is more than it's better to bin it first
Zip_Table=data.groupby('Zipcode').agg({'Sale_Price':'mean'}).sort_values('Sale_Price',ascending=True)
Zip_Table.head(10)
Zip_Table['Zipcode_Group']=pd.cut(Zip_Table['Sale_Price'],bins=10,
                                  labels=['Zipcode_Group_0',
                                         'Zipcode_Group_1',
                                         'Zipcode_Group_2',
                                         'Zipcode_Group_3',
                                         'Zipcode_Group_4',
                                         'Zipcode_Group_5',
                                         'Zipcode_Group_6',
                                         'Zipcode_Group_7',
                                         'Zipcode_Group_8',
                                         'Zipcode_Group_9'],
                                  include_lowest=True)
Zip_Table=Zip_Table.drop(columns='Sale_Price')
data=pd.merge(data,
              Zip_Table,
              left_on="Zipcode",
             how='left',
             right_index=True)
data=data.drop(columns="Zipcode")
data.head(10)
#this was categorical preprocessing
