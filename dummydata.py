import pandas as pd
import numpy as np
import random
import datetime

# Define the date range for the data
start_date = datetime.date(2019, 1, 1)
end_date = datetime.date(2022, 12, 31)

date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Create dummy data for products
products = ['Product A', 'Product B', 'Product C']
num_products = len(products)

# Initialize empty DataFrame
data = pd.DataFrame(columns=['Date', 'Product', 'Demand'])

# Generate dummy data
for date in date_range:
    for product in products:
        # Simulate demand as a random number (you can replace this with a more sophisticated demand generation method)
        demand = random.randint(50, 200)
        data = data.append({'Date': date, 'Product': product, 'Demand': demand}, ignore_index=True)

# Save the dummy data to a CSV file
data.to_csv('dummy_demand_data.csv', index=False)
