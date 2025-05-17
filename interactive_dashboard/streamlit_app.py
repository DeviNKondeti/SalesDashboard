import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Load and prepare data
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
df['tip_pct'] = (df['tip'] / df['total_bill']) * 100

# Sidebar filters
st.sidebar.title("Filter Options")
days = st.sidebar.multiselect("Day", df['day'].unique(), default=df['day'].unique())
time = st.sidebar.radio("Time of Day", df['time'].unique(), index=0)

filtered_df = df[(df['day'].isin(days)) & (df['time'] == time)]

st.title("💡 Interactive Restaurant Tips Dashboard")

st.markdown("Explore how total bill and tip behavior varies across days, time, and more.")

# Column layout
col1, col2 = st.columns(2)

# Avg Tip % by Day
with col1:
    st.subheader("Average Tip % by Day")
    avg_tip_day = filtered_df.groupby('day')['tip_pct'].mean().reset_index()
    fig1, ax1 = plt.subplots()
    sns.barplot(data=avg_tip_day, x='day', y='tip_pct', ax=ax1)
    st.pyplot(fig1)

# Tip % vs Total Bill
with col2:
    st.subheader("Tip % vs Total Bill")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=filtered_df, x='total_bill', y='tip_pct', hue='sex', ax=ax2)
    st.pyplot(fig2)

# Show filtered data table
st.subheader("📄 Filtered Data")
st.dataframe(filtered_df)
