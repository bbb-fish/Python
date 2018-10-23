import pandas as pd
import teradata
import datetime
from datetime import date, timedelta

currDate = date.today()
yyyymmdd = currDate.strftime('%Y%m%d')


#df = pd.read_csv('/home/ec2-user/fish/git/aws/anomaly_chtr_20181016.csv')
df = pd.read_csv('C:\\Users\\p2813634\\Development\\python\\data\\anomaly_chtr_20181016.csv')
print('CSV LOADED')
count_rows = df.shape[0]
print(df.head(5))
print(count_rows)

###############################################
## Data Type Manipulations to match Teradata ##
###############################################

#DATE ALGORITHM IS RUN AND RECORDS ARE SCORED
#RUN_DT = datetime.date(2018, 10, 18) #year, month, today
RUN_DT = datetime.datetime.today().strftime('%Y-%m-%d')
print(RUN_DT)

#DATE RECORD ADDED TO TERADATA TABLE
#CREATED_DT = datetime.date(2018, 10, 18) #year, month, today
CREATED_DT = datetime.datetime.today().strftime('%Y-%m-%d')

#ADJUST DATE FORMAT ON TUNING_EVNT_START_DT
df['TUNING_EVNT_START_DT'] = pd.to_datetime(df.TUNING_EVNT_START_DT)
df['TUNING_EVNT_START_DT'] = df['TUNING_EVNT_START_DT'].dt.strftime('%Y-%m-%d')

#SET TRANSACTION TYPE
#TRXTYPE = 'chtr'
TRXTYPE = 'nonchtr'
#print(TRXTYPE)

#CHANGE SCORES TO FLOAT
df['scores'] = df['scores'].astype(float)

#CHANGE ANOMALY COLUMNS TO INTO
df['anomaly'] = df['anomaly'].astype(int)
df['t_anomaly'] = df['t_anomaly'].astype(int)

df['TRXTYPE'] = 'nonchtr'
df['CREATED_DT'] = CREATED_DT
df['RUN_DT'] = RUN_DT
df['ANOMALY_FLAG'] = 1

df = df.drop(['DOW_INT','MOY_INT','DT_NBR'], axis=1)
df.columns = df.columns.str.upper()

df = df[['TRXTYPE','CREATED_DT','RUN_DT','MASDIV','STATION','TUNING_EVNT_START_DT','DOW','MOY','TRANSACTIONS',
         'SCORES','ANOMALY','T_ANOMALY','ANOMALY_FLAG']]

#######################
## SQLALCHEMY INSERT ##
#######################

from sqlalchemy import create_engine
user = 'E813634'
pwd = 'DQX1duds!'
host = '142.136.184.160'

td_engine = create_engine('teradata://'+ user +':' + pwd + '@'+ host + '/' + '?authentication=LDAP?database=DLABBUAnalytics_Lab')

print(df.head())
print(df.info())

df.to_sql(con=td_engine, name='Anomaly_Detection_SuperSet', if_exists='append', index=False, schema='DLABBUAnalytics_Lab')

df2 = pd.read_sql("select * from DLABBUAnalytics_Lab.Anomaly_Detection_SuperSet", td_engine)

print(df2)
