import pandas as pd
import os

################################################################
#READ IN THE PREDICTIONS FROM DATAROBOT CSV

dir = '/Users/rfisher/development/Churn/Data/ChurnModel2/'
#fname = 'my_churn_2018-10-05.csv'
fname = 'Predicted_PredApr18-12Mo.csv'

PredFile = pd.read_csv(dir + fname)

print(PredFile.head())
print(PredFile.info())

################################################################
#READ IN SYSCODES THAT ARE MAPPED TO CUST_KEY

dir = '/Users/rfisher/development/Churn/Data/ChurnModel2/'
#fname = 'my_churn_2018-10-05.csv'
fname = 'SyscodeMap.csv'

SysMap = pd.read_csv(dir + fname)

print(SysMap.head())
print(SysMap.info())

################################################################
# JOIN SYSCODE TO PREDICTION CUSTOMER KEYS
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html

OutputFile = PredFile.merge(SysMap, how='left', left_on='cust_key', right_on='CUST_KEY')

print(OutputFile.head())
print(OutputFile.info())

################################################################
# CREATE OUTPUT DATA SETS TO FEED INTO THE MODEL

filepath = '/Users/rfisher/development/Churn/Data/Output/'

out = 'JoinedSyscode.csv'


try:
    os.remove(filepath + out)
except OSError:
    pass

OutputFile.to_csv(filepath + out, index=False)
