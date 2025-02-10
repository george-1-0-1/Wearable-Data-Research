import pandas as pd

data = pd.read_csv("data.csv")

# Convert values to float, replacing non-numeric values with NaN
data["Geometry-Dash"] = pd.to_numeric(data["Geometry-Dash"], errors='coerce')
data["Clash-Royale"] = pd.to_numeric(data["Clash-Royale"], errors='coerce')

# Filter out values between 55 and 140 in both columns
filtered_data = data[(data["Geometry-Dash"] >= 55) & (data["Geometry-Dash"] <= 140) & 
                     (data["Clash-Royale"] >= 55) & (data["Clash-Royale"] <= 140)]

# Save the filtered data to another CSV file
filtered_data.to_csv("filtered_data.csv", index=False)
