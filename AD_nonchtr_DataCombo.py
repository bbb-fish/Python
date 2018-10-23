import pandas as pd
import pyodbc
import os

##########################
## DELETE PREVIOUS FILE ##
##########################

#Delete the 20 day file
if os.path.exists('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_20.csv'):
    os.remove('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_20.csv')
    print('20 deleted')
else:
    print('20 day file does not exist')

#Delete the 40 day file
if os.path.exists('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_40.csv'):
    os.remove('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_40.csv')
    print('40 deleted')
else:
    print('40 day file does not exist')

#Delete the 60 day file
if os.path.exists('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_60.csv'):
    os.remove('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_60.csv')
    print('60 deleted')
else:
    print('60 day file does not exist')

#Delete the 80 day file
if os.path.exists('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_80.csv'):
    os.remove('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_80.csv')
    print('80 deleted')
else:
    print('80 day file does not exist')

#Delete the 90 day file
if os.path.exists('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_90.csv'):
    os.remove('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_90.csv')
    print('90 deleted')
else:
    print('90 day file does not exist')

#Delete the SuperSet file
if os.path.exists('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_super.csv'):
    os.remove('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_super.csv')
    print('Super(nonchtr) deleted')
else:
    print('Super(nonchtr) file does not exist')

###################
## FIRST 20 DAYS ##
###################

#PULL FROM DATABASE AND CREATE DATAFRAME
sql_conn = pyodbc.connect('dsn=ConnectR')
query = "select masdiv, station, tuning_evnt_start_dt, dow, moy, transactions from (SELECT mas.mas_div_desc AS MASDIV, stn.stn_nm AS STATION, tuning_evnt_start_dt, cal.day_of_week_shrt_nm AS DOW, cal.clndr_mo_nm AS MOY, COUNT(am_tuning_evnt_key) AS TRANSACTIONS FROM prd_am_bi_1.am_program_tuning_event_fact ptef INNER JOIN prd_am_bi_1.am_calendar_dim cal ON ptef.tuning_evnt_start_dt = cal.clndr_dt INNER JOIN prd_am_bi_1.am_station_dim stn ON ptef.stn_key = stn.stn_key INNER JOIN prd_am_bi_1.am_mas_division_dim mas ON (ptef.mas_div_key = mas.mas_div_key and cal.CLNDR_SKEY between mas.EFF_START_DAY_KEY and mas.EFF_END_DAY_KEY) WHERE cal.clndr_dt >= current_date - 20 and mas.mas_div_desc not in ('Charter') GROUP BY tuning_evnt_start_dt, DOW, MOY, STATION, MASDIV) x;"
df = pd.read_sql(query, sql_conn)

#SHOW INFORMATION ON DATAFRAME
count_rows = df.shape[0]
print(count_rows)
print(df.head(10))

#SAVE THE DATA PULL AS A CSV
df.to_csv('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_20.csv')
print('20 SUCCESSFULLY WRITTEN TO CSV')

#############
## 40 DAYS ##
#############

#PULL FROM DATABASE AND CREATE DATAFRAME
sql_conn = pyodbc.connect('dsn=ConnectR')
query = "select masdiv, station, tuning_evnt_start_dt, dow, moy, transactions from (SELECT mas.mas_div_desc AS MASDIV, stn.stn_nm AS STATION, tuning_evnt_start_dt, cal.day_of_week_shrt_nm AS DOW, cal.clndr_mo_nm AS MOY, COUNT(am_tuning_evnt_key) AS TRANSACTIONS FROM prd_am_bi_1.am_program_tuning_event_fact ptef INNER JOIN prd_am_bi_1.am_calendar_dim cal ON ptef.tuning_evnt_start_dt = cal.clndr_dt INNER JOIN prd_am_bi_1.am_station_dim stn ON ptef.stn_key = stn.stn_key INNER JOIN prd_am_bi_1.am_mas_division_dim mas ON (ptef.mas_div_key = mas.mas_div_key and cal.CLNDR_SKEY between mas.EFF_START_DAY_KEY and mas.EFF_END_DAY_KEY) WHERE cal.clndr_dt < current_date - 20 and cal.clndr_dt >= current_date - 40 and mas.mas_div_desc not in ('Charter') GROUP BY tuning_evnt_start_dt, DOW, MOY, STATION, MASDIV) x;"
df = pd.read_sql(query, sql_conn)

#SHOW INFORMATION ON DATAFRAME
count_rows = df.shape[0]
print(count_rows)
print(df.head(10))

#SAVE THE DATA PULL AS A CSV
df.to_csv('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_40.csv')
print('40 SUCCESSFULLY WRITTEN TO CSV')

#############
## 60 DAYS ##
#############

#PULL FROM DATABASE AND CREATE DATAFRAME
sql_conn = pyodbc.connect('dsn=ConnectR')
query = "select masdiv, station, tuning_evnt_start_dt, dow, moy, transactions from (SELECT mas.mas_div_desc AS MASDIV, stn.stn_nm AS STATION, tuning_evnt_start_dt, cal.day_of_week_shrt_nm AS DOW, cal.clndr_mo_nm AS MOY, COUNT(am_tuning_evnt_key) AS TRANSACTIONS FROM prd_am_bi_1.am_program_tuning_event_fact ptef INNER JOIN prd_am_bi_1.am_calendar_dim cal ON ptef.tuning_evnt_start_dt = cal.clndr_dt INNER JOIN prd_am_bi_1.am_station_dim stn ON ptef.stn_key = stn.stn_key INNER JOIN prd_am_bi_1.am_mas_division_dim mas ON (ptef.mas_div_key = mas.mas_div_key and cal.CLNDR_SKEY between mas.EFF_START_DAY_KEY and mas.EFF_END_DAY_KEY) WHERE cal.clndr_dt < current_date - 40 and cal.clndr_dt >= current_date - 60 and mas.mas_div_desc not in ('Charter') GROUP BY tuning_evnt_start_dt, DOW, MOY, STATION, MASDIV) x;"
df = pd.read_sql(query, sql_conn)

#SHOW INFORMATION ON DATAFRAME
count_rows = df.shape[0]
print(count_rows)
print(df.head(10))

#SAVE THE DATA PULL AS A CSV
df.to_csv('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_60.csv')
print('60 SUCCESSFULLY WRITTEN TO CSV')

#############
## 80 DAYS ##
#############

#PULL FROM DATABASE AND CREATE DATAFRAME
sql_conn = pyodbc.connect('dsn=ConnectR')
query = "select masdiv, station, tuning_evnt_start_dt, dow, moy, transactions from (SELECT mas.mas_div_desc AS MASDIV, stn.stn_nm AS STATION, tuning_evnt_start_dt, cal.day_of_week_shrt_nm AS DOW, cal.clndr_mo_nm AS MOY, COUNT(am_tuning_evnt_key) AS TRANSACTIONS FROM prd_am_bi_1.am_program_tuning_event_fact ptef INNER JOIN prd_am_bi_1.am_calendar_dim cal ON ptef.tuning_evnt_start_dt = cal.clndr_dt INNER JOIN prd_am_bi_1.am_station_dim stn ON ptef.stn_key = stn.stn_key INNER JOIN prd_am_bi_1.am_mas_division_dim mas ON (ptef.mas_div_key = mas.mas_div_key and cal.CLNDR_SKEY between mas.EFF_START_DAY_KEY and mas.EFF_END_DAY_KEY) WHERE cal.clndr_dt < current_date - 60 and cal.clndr_dt >= current_date - 80 and mas.mas_div_desc not in ('Charter') GROUP BY tuning_evnt_start_dt, DOW, MOY, STATION, MASDIV) x;"
df = pd.read_sql(query, sql_conn)

#SHOW INFORMATION ON DATAFRAME
count_rows = df.shape[0]
print(count_rows)
print(df.head(10))

#SAVE THE DATA PULL AS A CSV
df.to_csv('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_80.csv')
print('80 SUCCESSFULLY WRITTEN TO CSV')

#############
## 90 DAYS ##
#############

#PULL FROM DATABASE AND CREATE DATAFRAME
sql_conn = pyodbc.connect('dsn=ConnectR')
query = "select masdiv, station, tuning_evnt_start_dt, dow, moy, transactions from (SELECT mas.mas_div_desc AS MASDIV, stn.stn_nm AS STATION, tuning_evnt_start_dt, cal.day_of_week_shrt_nm AS DOW, cal.clndr_mo_nm AS MOY, COUNT(am_tuning_evnt_key) AS TRANSACTIONS FROM prd_am_bi_1.am_program_tuning_event_fact ptef INNER JOIN prd_am_bi_1.am_calendar_dim cal ON ptef.tuning_evnt_start_dt = cal.clndr_dt INNER JOIN prd_am_bi_1.am_station_dim stn ON ptef.stn_key = stn.stn_key INNER JOIN prd_am_bi_1.am_mas_division_dim mas ON (ptef.mas_div_key = mas.mas_div_key and cal.CLNDR_SKEY between mas.EFF_START_DAY_KEY and mas.EFF_END_DAY_KEY) WHERE cal.clndr_dt < current_date - 80 and cal.clndr_dt >= current_date - 90 and mas.mas_div_desc not in ('Charter') GROUP BY tuning_evnt_start_dt, DOW, MOY, STATION, MASDIV) x;"
df = pd.read_sql(query, sql_conn)

#SHOW INFORMATION ON DATAFRAME
count_rows = df.shape[0]
print(count_rows)
print(df.head(10))

#SAVE THE DATA PULL AS A CSV
df.to_csv('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_90.csv')
print('90 SUCCESSFULLY WRITTEN TO CSV')

#COMBINE THE DATA PULLS TO CREATE 90 DAY DATASET AND SAVE AS CSV
df1 = pd.read_csv('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_20.csv')
print('1')
df2 = pd.read_csv('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_40.csv')
print('2')
df3 = pd.read_csv('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_60.csv')
print('3')
df4 = pd.read_csv('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_80.csv')
print('4')
df5 = pd.read_csv('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_90.csv')
print('5')
frames = [df1,df2,df3,df4,df5]
super = pd.concat(frames)
count_rows = super.shape[0]
print(count_rows)
super.to_csv('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_super.csv')
print('SUPERSET SUCCESSFULLY WRITTEN TO CSV')
