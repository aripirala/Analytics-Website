import pyodbc

# Create Connection to SQL Server, using Windows Login Credentials
con = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server}',server = 'bhxsql2014-dev', database = 'BMAnalytics')
 
# Create DataFrame using SQL Statement   
df = pd.read_sql(" Select * From dbo.EUActiveStores ", con)

# Output to Excel
writer = pd.ExcelWriter('W:\B&M\Store Segmentation\Pete\Learning\Python\SampleData\df.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()


