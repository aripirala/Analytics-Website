import pyodbc
import pandas as pd

#store = float(input('Enter Store No : '))

# Create Connection to SQL Server, using Windows Login Credentials
con = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server}',server = 'bhxsql2014-dev', database = 'BMAnalytics')
 
# Create DataFrame using SQL Statement   
df = pd.read_sql(" Select * from dbo.EUActiveStores where [Store No] = ? ", con, params={float(input('Enter Store No : '))})

print(df)