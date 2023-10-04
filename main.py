import pyproj
import pandas as pd

df = pd.read_csv("D://Assignment_Garudalytics//application//static//OCO-2_2014_11_1.csv")

# Define the source and target projections
source_proj = pyproj.Proj(init='epsg:4326')  # WGS 84 (latitude and longitude)
target_proj = pyproj.Proj(init='epsg:3857')  # Web Mercator

# Convert the latitude and longitude columns to the target projection
df['Latitude'], df['Longitude'] = pyproj.transform(source_proj, target_proj, df['Longitude'].values, df['Latitude'].values)

# Save the updated DataFrame to a new CSV file
df.to_csv('OCO-2_2014_11_1.csv', index=False)