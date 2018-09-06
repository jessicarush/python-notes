'''Pandas - Python Data Analysis Library'''

# http://pandas.pydata.org/

# The pandas library allows you to take in data from a variety of sources
# (ie JSON, CSV, excel, from data mining activities such as web scraping),
# then analyze the data in python and then output the results (ie tables,
# or data visualization – with the help of additional libraries such as bokeh).

# $ pip3 install pandas

# NOTE: Jupyter Notebook is a helpful tool for this kind of work.
# see jupyter_notebook.py

import pandas


# Creating a DataFrame
# -----------------------------------------------------------------------------
# Create a DataFrame, which is a special kind of object that will hold data.
# Think of a DataFrame as a table. You pass a list of lists to a DataFrame,
# where each list is like a row.

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]])

print(type(df1))
# <class 'pandas.core.frame.DataFrame'>
print(df1)
#     0   1   2
# 0   2   4   6
# 1  10  20  30

df1 = df1.append([[50, 70, 80]])
print(df1)
#     0   1   2
# 0   2   4   6
# 1  10  20  30
# 0  50  70  80

# The numbers 0, 1 beside each row are the indexes for the rows. The numbers
# 0, 1, 2 at the top are the names of the columns. You can create your own
# column names by passing a list of values to the columns arg:

col_names = ['A', 'B', 'C']
df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=col_names)

print(df1)
#     A   B   C
# 0   2   4   6
# 1  10  20  30

# You can also create your own index names. However, you will usually leave
# index at its default numbering (typically a data set will have a fixed number
# of columns but many, many, many rows).

cols = ['A', 'B', 'C']
rows = ['one', 'two']
df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=cols, index=rows)

print(df1)
#        A   B   C
# one    2   4   6
# two   10  20  30

# You can also create a DataFrame by passing a list of dictionaries:

person1 = {'First': 'Rick', 'Last': 'Sanchez', 'Email': 'abc'}
person2 = {'First': 'Morty', 'Last': 'Sanchez', 'Email': 'xyz'}
df2 = pandas.DataFrame([person1, person2])

print(df2)
#   Email  First     Last
# 0   abc   Rick  Sanchez
# 1   xyz  Morty  Sanchez


# Reading data from files
# -----------------------------------------------------------------------------
# As mentioned, pandas can read a wide range of data files using methods
# specific to each data type. The read methods in pandas include:

read_methods = ['read_clipboard', 'read_csv', 'read_excel', 'read_feather',
'read_fwf', 'read_gbq', 'read_hdf', 'read_html', 'read_json', 'read_msgpack',
'read_parquet', 'read_pickle', 'read_sas', 'read_sql', 'read_sql_query',
'read_sql_table', 'read_stata', 'read_table']

# Example:
df1 = pandas.read_csv('data/supermarkets.csv')

# Note that with CSV files, pandas and python will assume the first row is
# a header row. If it isn't, set the header arg to None:

df1 = pandas.read_csv('data/supermarkets.csv', header=None)

# In terms row indexes, python adds it's own index column (0–?). If the dataset
# happens to already include an index type column, you can tell python to use
# this as the index by passing the column header name to the set_index() method.
# Note this is easier to see using Jupyter (see below).

df1 = pandas.read_csv('data/supermarkets.csv')
df1.set_index('ID')

# Note that the set_index method is like the sorted() method in that it doesn't
# change the original DataFrame. If you want to do this permanently, you would
# have to do a reassignment:

df1 = pandas.read_csv('data/supermarkets.csv')
df1 = df1.set_index('ID')

# Alternatively, the set_index method takes a inplace parameter which is set to
# False by default. If we set it to True, it will do the same as above:

df1 = pandas.read_csv('data/supermarkets.csv')
df1.set_index('ID', inplace=True)

# Incidentally, you can retrieve the column names and index names via their
# own methods:

print(df1.columns)
# Index(['Address', 'City', 'State', 'Country', 'Name', 'Employees'], dtype='object')
print(type(df1.columns))
# <class 'pandas.core.indexes.base.Index'>
print(df1.index)
# Int64Index([1, 2, 3, 4, 5, 6], dtype='int64', name='ID')
print(type(df1.index))
# <class 'pandas.core.indexes.numeric.Int64Index'>

# This method returns the total number of rows, columns in the DataFrame:

print(df1.shape)
# (6, 7)

# These methods also work for json files:
df2 = pandas.read_json('data/supermarkets.json')

# For Excel files, it's best to pass an additional arg:
df3 = pandas.read_excel('data/supermarkets.xlsx', sheet_name=0)

# Since Excel files can have more than one sheet, the sheet_name arg lets
# python know the index of the sheet. Obviously if the file had 3 sheets and we
# wanted to access the 3rd we'd say sheet_name=2

# If you have a plain text file that uses commas, use the csv read method:
df4 = pandas.read_csv('data/supermarkets-commas.txt')

# If you have a plain text file that uses some other separator, add the arg:
df5 = pandas.read_csv('data/supermarkets-semicolons.txt', sep=';')

# If your data file lives on the web, just insert the URL:
df6 = pandas.read_csv('http://pythonhow.com/supermarkets.csv')


# Accessing DataFrame rows, columns: slicing
# -----------------------------------------------------------------------------
# First of all, you can access individual columns by using dot notation:

print(type(df1.Name))
# <class 'pandas.core.series.Series'>

print(df1.Name)
# 0        Madeira
# 1    Bready Shop
# 2    Super River
# 3     Ben's Shop
# 4        Sanchez
# 5     Richvalley
# Name: Name, dtype: object

# To access a row or section, it's a little different. We can use label-based
# indexing (loc[]) or position-based indexing (iloc[]).
# The general syntax rule for all is:

# df.loc[startrow:endrow, startcolumn:endcolumn]
# df.iloc[startrow:endrow, startcolumn:endcolumn]

# This gives you a range of cells:
print(df1.loc[2:3, 'Address':'State'])
#            Address           City             State
# ID
# 2   735 Dolores St  San Francisco          CA 94119
# 3      332 Hill St  San Francisco  California 94114

# This gives you a whole row:
print(df1.loc[2:2,:])
#            Address           City     State Country         Name  Employees
# ID
# 2   735 Dolores St  San Francisco  CA 94119     USA  Bready Shop         15

# This gives you a single cell:
print(df1.loc[3, 'Name'])
# Super River

# This gives you a whole column like above:
print(df1.loc[:,'Name'])
# ID
# 1        Madeira
# 2    Bready Shop
# 3    Super River
# 4     Ben's Shop
# 5        Sanchez
# 6     Richvalley
# Name: Name, dtype: object

# With position-based indexing, there are two things to remember:
# 1. The index numbering starts at 0 not counting the index and header columns
# 2. The slices work just like list slices in terms of the the second number
#    in the range is up to but not included.

print(df1.iloc[1:3, 4:6])
#            Name  Employees
# ID
# 2   Bready Shop         15
# 3   Super River         25


# Deleting data
# -----------------------------------------------------------------------------
# to delete a column, pass 1 after the column name:
print(df1.drop('Country', 1))
#             Address           City             State         Name  Employees
# ID
# 1      3666 21st St  San Francisco          CA 94114      Madeira          8
# 2    735 Dolores St  San Francisco          CA 94119  Bready Shop         15
# 3       332 Hill St  San Francisco  California 94114  Super River         25
# 4      3995 23rd St  San Francisco          CA 94114   Ben's Shop         10
# 5   1056 Sanchez St  San Francisco        California      Sanchez         12
# 6   551 Alvarado St  San Francisco          CA 94114   Richvalley         20

# to delete a row, pass 0 after the index name:
print(df1.drop(3, 0))
#             Address           City       State Country         Name Employees
# ID
# 1      3666 21st St  San Francisco    CA 94114     USA      Madeira         8
# 2    735 Dolores St  San Francisco    CA 94119     USA  Bready Shop        15
# 4      3995 23rd St  San Francisco    CA 94114     USA   Ben's Shop        10
# 5   1056 Sanchez St  San Francisco  California     USA      Sanchez        12
# 6   551 Alvarado St  San Francisco    CA 94114     USA   Richvalley        20

# Note once again, the drop method does not change the DataFrame in place.


# Adding/changing data
# -----------------------------------------------------------------------------
# To add a row:
df1= df1.append({'Address': '124 Main St', 'City': 'Vancouver', 'State': 'BC',
  'Country': 'Canada', 'Name' :'Kins', 'Employees': 10}, ignore_index=True)

print(df1.loc[:,'Name':])
#           Name  Employees
# 0      Madeira          8
# 1  Bready Shop         15
# 2  Super River         25
# 3   Ben's Shop         10
# 4      Sanchez         12
# 5   Richvalley         20
# 6         Kins         10

# To add a column:
websites = ['madeira.com', 'bready.com', None, None, None, None, None]
df1['website'] = websites

print(df1.loc[:,'Name':'website'])
#           Name  Employees      website
# 0      Madeira          8  madeira.com
# 1  Bready Shop         15   bready.com
# 2  Super River         25         None
# 3   Ben's Shop         10         None
# 4      Sanchez         12         None
# 5   Richvalley         20         None
# 6         Kins         10         None

# You can reassign a column in the same way:
df1['Country'] = ['US'] * 7

print(df1.loc[:,'Country':'Name'])
#   Country         Name
# 0      US      Madeira
# 1      US  Bready Shop
# 2      US  Super River
# 3      US   Ben's Shop
# 4      US      Sanchez
# 5      US   Richvalley
# 6      US         Kins

# Another way to add a new row by just providing a list instead of a dict,
# is to transpose your DataFrame with the T() method. This keeps the ID
# numbers in tact too. Let's reset the dataframe first:

df1 = pandas.read_csv('data/supermarkets.csv')
df1.set_index('ID', inplace=True)

df1_t = df1.T

print(df1_t)
# ID                     1               2                 3     etc..
# Address     3666 21st St  735 Dolores St       332 Hill St
# City       San Francisco   San Francisco     San Francisco
# State           CA 94114        CA 94119  California 94114
# Country               US              US                US
# Name             Madeira     Bready Shop       Super River
# Employees              8              15                25

# than add the new row as if it were a column:
row = ['124 Main St', 'Vancouver', 'BC', 'Canada', 'Kins', 10]
df1_t[7] = row

# then transpose it back:
df1 = df1_t.T

print(df1.loc[:,'Country':'Name'])
#    Country         Name
# ID
# 1       US      Madeira
# 2       US  Bready Shop
# 3       US  Super River
# 4       US   Ben's Shop
# 5       US      Sanchez
# 6       US   Richvalley
# 7   Canada         Kins

# To change a single cell, use .iat[] or .at[] dot notation. Apparently there's
# also a set_value() method but its marked for deprecation.
# – .at[] is similar to .loc[], in that it's a label-based lookup.
# – .iat[] is similar to .iloc[], in that it's an integer-based lookup.

df1.at[3, 'State'] = 'CA 94114'
df1.iat[4, 2] = 'CA 94114'


# Create a new column using data from other columns
# -----------------------------------------------------------------------------

df1['Full_Address'] = (df1['Address'] + ', ' + df1['City'] + ', '
                       + df1['State'] + ', ' + df1['Country'])

print(df1['Full_Address'])
# ID
# 1       3666 21st St, San Francisco, CA 94114, US
# 2     735 Dolores St, San Francisco, CA 94119, US
# 3        332 Hill St, San Francisco, CA 94114, US
# 4       3995 23rd St, San Francisco, CA 94114, US
# 5    1056 Sanchez St, San Francisco, CA 94114, US
# 6    551 Alvarado St, San Francisco, CA 94114, US
# 7              124 Main St, Vancouver, BC, Canada


# Use pandas apply() method to run a function on data values
# -----------------------------------------------------------------------------
# This example uses the geopy module to produce latitude and longitudes.
# see geopy_module.py

from geopy.geocoders import Nominatim

geolocator = Nominatim(scheme='http')

df1['g'] = df1['Full_Address'].apply(geolocator.geocode)

print(df1.g[1].latitude)   # 37.7570511
print(df1.g[1].longitude)  # -122.4188036

df1['latitude'] = df1['g'].apply(lambda x: x.latitude if x != None else None)
df1['longitude'] = df1['g'].apply(lambda x: x.longitude if x != None else None)

df1 = df1.drop('g', 1)
df1 = df1.drop('website', 1)
#                                     Full_Address   latitude   longitude
# ID
# 1      3666 21st St, San Francisco, CA 94114, US  37.757051 -122.418804
# 2    735 Dolores St, San Francisco, CA 94119, US        NaN         NaN
# 3       332 Hill St, San Francisco, CA 94114, US  37.756102 -122.421041
# 4      3995 23rd St, San Francisco, CA 94114, US  37.752965 -122.431714
# 5   1056 Sanchez St, San Francisco, CA 94114, US  37.748362 -122.429346
# 6   551 Alvarado St, San Francisco, CA 94114, US  37.753666 -122.434440
# 7             124 Main St, Vancouver, BC, Canada  49.159131 -122.934892


# Other DataFrame Methods
# -----------------------------------------------------------------------------
c = ['A','B','C']
df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30], [500, 700, 900]], columns=c)
print(df1)
#      A    B    C
# 0    2    4    6
# 1   10   20   30
# 2  500  700  900

print(dir(df1))
# There are 214 non-private methods for DataFrames.
# These are just a few examples.

print(df1.mean())        # gives you the mean of all the columns
print(type(df1.mean()))  # <class 'pandas.core.series.Series'>
# 0    170.666667
# 1    241.333333
# 2    312.000000
# dtype: float64

print(df1.mean().mean()) # gives you the mean of the entire DataFrame
# 241.333333333
print(df1.B.median())
# 20.0
print(df1.B.min())
# 4
print(df1.B.max())
# 700
