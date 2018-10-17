import pandas as pd
import pyodbc

#PULL FROM DATABASE AND CREATE DATAFRAME
#sql_conn = pyodbc.connect('dsn=ConnectR')
#query = "select masdiv, station, tuning_evnt_start_dt, dow, moy, transactions from (SELECT mas.mas_div_desc AS MASDIV, stn.stn_nm AS STATION, tuning_evnt_start_dt, cal.day_of_week_shrt_nm AS DOW, cal.clndr_mo_nm AS MOY, COUNT(am_tuning_evnt_key) AS TRANSACTIONS FROM prd_am_bi_1.am_program_tuning_event_fact ptef INNER JOIN prd_am_bi_1.am_calendar_dim cal ON ptef.tuning_evnt_start_dt = cal.clndr_dt INNER JOIN prd_am_bi_1.am_station_dim stn ON ptef.stn_key = stn.stn_key INNER JOIN #prd_am_bi_1.am_mas_division_dim mas ON (ptef.mas_div_key = mas.mas_div_key and cal.CLNDR_SKEY between mas.EFF_START_DAY_KEY and mas.EFF_END_DAY_KEY) WHERE cal.clndr_dt < current_date - 80 and cal.clndr_dt >= current_date - 90 and mas.mas_div_desc not in ('Charter') GROUP BY tuning_evnt_start_dt, DOW, MOY, STATION, MASDIV) x;"
#df = pd.read_sql(query, sql_conn)

#SHOW INFORMATION ON DATAFRAME
#count_rows = df.shape[0]
#print(count_rows)
#print(df.head(10))

#SAVE THE DATA PULL AS A CSV
#df.to_csv('C:\\Users\\p2813634\\Development\\python\\teradata\\nonchtr_90.csv')
#print('SUCCESSFULLY WRITTEN TO CSV')

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
print('SUCCESSFULLY WRITTEN TO CSV')
