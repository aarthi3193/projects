import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

df_yellow = pd.read_csv('yellow_tripdata_2017-06.csv',engine='python')
df_yellow['cab_type'] = 'yellow'

#since I am merging the two datasets for both green and yellow cab I am renaming the columns into the same title
df_yellow.rename(columns={'tpep_pickup_datetime': 'pickup_datetime', 'tpep_dropoff_datetime': 'dropoff_datetime'}, inplace=True)

df_yellow.head()

df_green = pd.read_csv('green_tripdata_2017-06.csv',engine='python')
df_green['cab_type'] = 'green'
df_green.rename(columns={'lpep_pickup_datetime': 'pickup_datetime', 'lpep_dropoff_datetime': 'dropoff_datetime'}, inplace=True)

df_green.head()


#merging two data sets for the month of june
frames = [df_yellow,df_green]
df1 = pd.concat(frames)
df1['cab_type'].value_counts()
df1.head()

#Remove the missing values
df1.dropna()

# Print the size of the dataset
print "Number of rows:", df1.shape[0]
print "Number of columns: ", df1.shape[1]

#converting the pickup date and pickup time to datetime objects
df1['pickup_datetime'] = df1['pickup_datetime'].apply(lambda x:datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
df1['dropoff_datetime'] = df1['dropoff_datetime'].apply(lambda x:datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))


#To calculate the number of people who take green or yellow can daily throughout the month of June 2107

df1['pickup_date'] = [datetime.datetime.date(d) for d in df1['pickup_datetime']]
df1['pickup_date'].head()
plt.figure(figsize=(12,6))
ax1 = sns.countplot(x="pickup_date", hue="cab_type", data=df1,order=df1['pickup_date'].value_counts().index)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.show()
print'**'


#To calculate the average trip distance covered by the cabs for a day - grouping the values and plotting
df1[['trip_distance','cab_type']].groupby('cab_type').mean().plot.bar()
plt.title('Mean trip distance across day')
plt.show()
print'**'


# To plot the peak hour of the day -To find the peak time of the day (morning or evening?)
df1['pickup_hour'].value_counts(sort = False).plot.bar()
plt.xlabel("Hour")
plt.ylabel("counts")
plt.show()
print'**'

df1['pickup_hour'] = df1['pickup_datetime'].apply(lambda x: x.hour)
ax2 = sns.countplot(x="pickup_hour", hue="cab_type", data=df1)
plt.xlabel("Hour")
plt.ylabel("counts")
plt.show()


# To calulate the number of trips and the average fair charged to/from NYC airports
airports_trips = df1[(df1.RatecodeID==2) | (df1.RatecodeID==3)]
print "Number of trips to/from NYC airports: ", airports_trips.shape[0]
print "Average fare (calculated by the meter) of trips to/from NYC airports: $", airports_trips.fare_amount.mean(),"per trip"
print "Average total charged amount (before tip) of trips to/from NYC airports: $", airports_trips.total_amount.mean(),"per trip"
print '**'

# To calculate the tip percentage
df1['tip_percent'] = 100 * df1['tip_amount']/df1['fare_amount']
print((df1['tip_percent']).value_counts().head())
