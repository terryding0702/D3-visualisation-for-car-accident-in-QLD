import pandas as pd

# Month conversion
monthdict = {'January':'01',
            'February':'02',
            'March':'03',
            'April':'04',
            'May':'05',
            'June':'06',
            'July':'07',
            'August':'08',
            'September':'09',
            'October':'10',
            'November':'11',
            'December':'12'
             }

# Define useful columns
usecols = ['Crash_Year', 'Crash_Month','Crash_Day_Of_Week', 'Crash_Hour', 'Crash_Type',
       'Crash_Longitude_GDA94', 'Crash_Latitude_GDA94','Loc_ABS_Statistical_Area_4',
       'Loc_Federal_Electorate','Loc_ABS_Remoteness', 'Count_Casualty_Fatality',
       'Count_Casualty_Hospitalised', 'Count_Casualty_MedicallyTreated',
       'Count_Casualty_MinorInjury', 'Count_Casualty_Total','Crash_Speed_Limit']
# read .csv file
df = pd.read_csv('locations.csv')
# Delete contains empty rows
df.dropna(axis = 0)
# Delete contains duplicate line
df = df.drop_duplicates()
# Get all columns of data
#columns = (df.columns)
#print(columns)

# Filter data based on useful columns
df = df[usecols]

# Eliminate wrong data in latitude and longitude
df = df[(df['Crash_Longitude_GDA94']!=0.0)&(df['Crash_Latitude_GDA94']!=0.0)]

# Add a column for the data, year and month (eg 201801), used to draw the timeline, change the day of the week to adjust ordering
date = []
for idx,row in df.iterrows():
    year = row['Crash_Year']
    month = row['Crash_Month']
    date.append(str(year)+monthdict[month])

df['Crash_Date'] = date
#print(df)

# Save data to file
df.to_csv('locations-do.csv')
# Save the first 30000 line
#df[:30000].to_csv('locations-do-3.csv')
