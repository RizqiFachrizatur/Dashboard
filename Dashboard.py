import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Theme Dashboard
st.set_page_config(page_title="Bike Rental Analysis", page_icon="🚴", layout="wide")

# Load data dari file CSV yang telah di-upload
df_day = pd.read_csv(('https://raw.githubusercontent.com/RizqiFachrizatur/Dasboard/refs/heads/main/day.csv'))

# Konversi kolom 'dteday' ke datetime jika belum
df_day['dteday'] = pd.to_datetime(df_day['dteday'])

# Title & Icon
st.title("🚴 Bike Rental Analysis")
st.markdown("### Analyzing the Impact of Weather and User Type on Bike Rentals")

# Sidebar untuk filter tahun
st.sidebar.title("Filter Data")
st.sidebar.markdown("Use the filter below to customize the data view:")
year_filter = st.sidebar.selectbox("Select Year", [2011, 2012])

# Filter data berdasarkan tahun
if year_filter == 2011:
    filtered_data = df_day[df_day['yr'] == 0]
else:
    filtered_data = df_day[df_day['yr'] == 1]

# Header untuk pertanyaan pertama
st.markdown("## 🌡️ How Weather Affects Bike Rentals")

# Scatter plot untuk pengaruh temperature dan humidity terhadap total rentals
st.markdown("### Temperature vs Total Rentals")
fig_temp, ax_temp = plt.subplots()
sns.scatterplot(x='temp', y='cnt', data=filtered_data, ax=ax_temp, color='#3498DB')
ax_temp.set_title('Impact of Temperature on Total Bike Rentals', fontsize=16)
ax_temp.set_xlabel('Temperature (Normalized)', fontsize=12)
ax_temp.set_ylabel('Total Rentals', fontsize=12)
plt.grid(True)
st.pyplot(fig_temp)

# Grafik kedua untuk humidity
st.markdown("### Humidity vs Total Rentals")
fig_hum, ax_hum = plt.subplots()
sns.scatterplot(x='hum', y='cnt', data=filtered_data, ax=ax_hum, color='#E74C3C')
ax_hum.set_title('Impact of Humidity on Total Bike Rentals', fontsize=16)
ax_hum.set_xlabel('Humidity (Normalized)', fontsize=12)
ax_hum.set_ylabel('Total Rentals', fontsize=12)
plt.grid(True)
st.pyplot(fig_hum)

# Spacer between sections
st.markdown("<br><hr><br>", unsafe_allow_html=True)

# Header untuk pertanyaan kedua
st.markdown("## 🧑‍🤝‍🧑 Casual Users vs Registered Users Across Seasons")

# Bar plot perbandingan rentals berdasarkan user type dan season
season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
filtered_data['season'] = filtered_data['season'].map(season_map)

# Total rentals by user type and season
user_season_data = filtered_data.groupby(['season'])[['casual', 'registered']].sum().reset_index()

# Plot untuk user type per season
st.markdown("### Total Rentals by Casual and Registered Users Across Seasons")
fig_user, ax_user = plt.subplots()
user_season_data.plot(kind='bar', x='season', stacked=True, ax=ax_user, color=['#3498DB', '#E74C3C'])
ax_user.set_title('Total Rentals by Casual and Registered Users', fontsize=16)
ax_user.set_xlabel('Season', fontsize=12)
ax_user.set_ylabel('Total Rentals', fontsize=12)
plt.xticks(rotation=0)
st.pyplot(fig_user)

# Spacer before footer
st.markdown("<br><hr><br>", unsafe_allow_html=True)

# Footer
st.markdown("### Analysis by Rizqi Fachrizatur R")
