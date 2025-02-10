import pandas as pd
import numpy as np
from tqdm import tqdm

# Load the existing data
data = pd.read_csv("filtered_data.csv")

# Desired size of the dataset
desired_size = 1000000

# Calculate the number of times to repeat the existing data to reach the desired size
num_repeats = int(np.ceil(desired_size / len(data)))

# Repeat the existing data to reach the desired size
augmented_data = pd.concat([data] * num_repeats, ignore_index=True)

# Apply data augmentation techniques to the columns

# Time Warping: Randomly shuffle the time indices of each time series
for col in tqdm(data.columns, desc="Applying Time Warping"):
    augmented_data[col] = np.random.permutation(augmented_data[col])

# Additive Noise: Add random noise to each time series
noise_scale = 0.1  # Adjust the scale of the noise based on your data characteristics
for col in tqdm(data.columns, desc="Applying Additive Noise"):
    augmented_data[col] += np.random.normal(loc=0, scale=noise_scale, size=len(augmented_data))

# Time Shifting: Shift each time series by a random amount
max_shift = 10  # Maximum number of time steps to shift
for col in tqdm(data.columns, desc="Applying Time Shifting"):
    shift_amount = np.random.randint(-max_shift, max_shift)
    augmented_data[col] = np.roll(augmented_data[col], shift_amount)

# Truncate the dataset to the desired size
augmented_data = augmented_data.head(desired_size)

# Save the augmented data to a new CSV file
augmented_data.to_csv("augmented_data.csv", index=False)
