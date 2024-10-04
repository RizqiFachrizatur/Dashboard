import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
day_data = pd.read_csv('')

# Title of the app
st.title('Bike Rental Analysis: Weather & User Behavior')

# Section 1: Impact of Temperature and Humidity on Total Rentals
st.header('1. Impact of Temperature and Humidity on Total Rentals')

# Scatter plots for temperature vs total rentals and humidity vs total rentals
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Temperature vs Total Rentals
sns.scatterplot(ax=axes[0], x=day_data['temp'], y=day_data['cnt'], color='blue')
axes[0].set_title('Temperature vs Total Rentals')
axes[0].set_xlabel('Temperature (Normalized)')
axes[0].set_ylabel('Total Rentals')

# Humidity vs Total Rentals
sns.scatterplot(ax=axes[1], x=day_data['hum'], y=day_data['cnt'], color='green')
axes[1].set_title('Humidity vs Total Rentals')
axes[1].set_xlabel('Humidity (Normalized)')
axes[1].set_ylabel('Total Rentals')

st.pyplot(fig)

# Correlation between temperature, humidity, and total rentals
st.subheader('Correlation Analysis')
correlation = day_data[['temp', 'hum', 'cnt']].corr()
st.write(correlation)

# Section 2: Casual vs Registered Users Across Seasons
st.header('2. Casual vs Registered Users Across Seasons')

# Boxplot to show distribution of casual and registered users by season
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Casual users by season
sns.boxplot(ax=axes[0], x=day_data['season'], y=day_data['casual'], palette='Blues')
axes[0].set_title('Casual Users by Season')
axes[0].set_xlabel('Season (1: Winter, 2: Spring, 3: Summer, 4: Fall)')
axes[0].set_ylabel('Casual Users')

# Registered users by season
sns.boxplot(ax=axes[1], x=day_data['season'], y=day_data['registered'], palette='Greens')
axes[1].set_title('Registered Users by Season')
axes[1].set_xlabel('Season (1: Winter, 2: Spring, 3: Summer, 4: Fall)')
axes[1].set_ylabel('Registered Users')

st.pyplot(fig)

# Mean and median comparison for casual vs registered users
st.subheader('Statistical Comparison: Casual vs Registered Users')
casual_mean = day_data.groupby('season')['casual'].mean()
registered_mean = day_data.groupby('season')['registered'].mean()

st.write('Mean Casual Users by Season:', casual_mean)
st.write('Mean Registered Users by Season:', registered_mean)
