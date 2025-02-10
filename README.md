# Wearable-Data-Research
An application of using wearable devices to analyse and study swell data

## Application 

Time Series Analysis of Heart Rate for Stress Prognosis in Mobile Video Game Genres

## Workflow 

![image](https://github.com/user-attachments/assets/d441788b-a820-4440-86d9-dc3d183931a1)

## Overview of the PatchTST model architecture 

![image](https://github.com/user-attachments/assets/17466974-8452-4dd2-95a9-e8fd7cc06e8a)
![image](https://github.com/user-attachments/assets/85a42944-e23d-46fa-96e5-ec3c3720d50b)

## Data Collection and Preprocessing

The data was primarily collected in two very popular mobile video games of different genres, Clash Royale and Geometry Dash. Clash Royale is a real time strategy game developed by Supercell. It involves elements of collectible card games, tower defence and a multiplayer online battle arena. This game was selected as it would provide a variation in readings as no game is the same with each player reacting to different scenarios differently. This results in pure randomness of the heart rate for different people. The next game selected was Geometry Dash a music platformer developed by Robert Topala. This game was selected because it involves level design, each user was made to play the level this would help in providing a variational heart rate for different players for the exact same scenario. Our primary age demographic was between 18-21 years of age.

The average match length of a Clash Royale game is about 2 minutes so we ensured that uniformity was imparted to collecting the data for Geometry Dash as well. We collected the data for 15 players which resulted in about 50000 rows for each game and using data augmentation techniques and expanded the dataset to 1 million readings. Data augmentation is the process of artificially generating data from existing data. It helps provide a more robust dataset for training models that are not large in size and has showed its importance and efficacy in all scenarios. 

Then data was the preprocessed. As the sensor takes time to calibrate, we eliminate	all heart rate readings below 55.00 BPM.  This would ensure readings that are more accurate to human life. We finally store all values in a CSV file as seen Table 1 with 1 million rows for each game.

The dataset is unique when compared to other datasets present on video games as they are solely concentrated or targeted on either computer games or games that depend on joysticks like consoles or arcades.

## Training and Results

For the training part we perform a time series prediction and analysis on the two game datasets. We use compare PatchTST to the very popular Linear Regression. 
In linear regression, the relationship between a target variable denoted by y and a predictor variable denoted by x is represented by the following equation:
y = β₀ + β₁x + ε
where:
•	β₀ (beta-nought) is the y-intercept. This is the point where the regression line crosses the y-axis.
•	β₁ (beta-one) is the slope of the regression line. This value indicates the change in y for each unit change in x.
•	ε (epsilon) is the error term. This represents the difference between the predicted value of y and the actual value of y.
The goal of simple linear regression is to estimate the values of β₀ and β₁ that minimize the error between the predicted values of y and the actual values of y.
Using the NVIDIA P100 we predict values using both algorithms and plot them with their actual values using matplotlib. Training and all codes were written within PyTorch [15] and HuggingFace Transformers [16].


![image](https://github.com/user-attachments/assets/6f747782-6e32-4206-9e33-9c51d3efd46e)
Plot of PatchTST (Actual vs Predicted) for both Clash Royale and Geometry Dash

![image](https://github.com/user-attachments/assets/2f1a83c8-7af6-4c9e-9a39-40c92125fcb9)
Plot of Linear Regression (Actual vs Real) for Clash Royale 

![image](https://github.com/user-attachments/assets/2245b070-da24-4387-ade5-3d326890de6b)
Plot of Linear Regression (Actual vs Real) for Geometry Dash

In Figure 5 the linear regression model struggles to capture the high degree of volatility and rapid fluctuations in the actual Geometry-Dash BPM values. While it can track the overall trend, the linear regression predictions appear smoother and less responsive to the sudden spikes and drops in the actual data. In contrast, in Figure 3 PatchTST seems to perform better at tracking the sharp changes and volatility in the Geometry Dash BPM values compared to the linear regression. The transformer model's predictions are more aligned with the sudden fluctuations in the actual data, suggesting it may be better equipped to model the complex dynamics of this time series.

Similar to Geometry-Dash, the linear regression model in Figure 4 has difficulty fully capturing the rapid changes and volatility in the actual Clash-Royale BPM values. The linear regression predictions tend to be more muted and less responsive to the sudden spikes and drops in the actual data. For the Clash-Royale data, in Figure 3 PatchTST also appears to outperform the linear regression in terms of tracking the volatility and fluctuations in the actual BPM values. The transformer model's predictions are more closely aligned with the sharp changes observed in the Clash-Royale time series.

Overall, the comparison suggests that PatchTST is the better-performing approach for these types of volatile time series data representing BPM values in gaming contexts. The transformer model's ability to capture the rapid fluctuations and complex dynamics seems to provide an advantage over the linear regression model. This could be particularly relevant in the context of stress analysis, as the PatchTST's enhanced tracking of the BPM volatility may better reflect the user's emotional and cognitive states during gameplay. However, further quantitative evaluation and validation would be needed to confirm the relative performance and suitability of these models for stress-aware gaming applications.
