import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
df = pd.read_csv("cleaned_dataset.csv")

# Title
st.title("Sales Performance Dashboard")

st.write("Interactive dashboard for deep-dive sales analysis")

# KPI Calculations
total_sales = df["Sales"].sum()
total_orders = df["Order ID"].nunique()
avg_order_value = total_sales / total_orders

top_category = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

# KPI Cards

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Orders", total_orders)
col3.metric("Average Order Value", f"${avg_order_value:,.2f}")
col4.metric("Top Category", top_category)


# Filters

st.sidebar.header("Filters")

region_filter = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

category_filter = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)


filtered_df = df[
    (df["Region"].isin(region_filter)) &
    (df["Category"].isin(category_filter))
]


# Category Chart

category_sales = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    title="Sales by Category"
)

st.plotly_chart(fig1)


# Region Chart

region_sales = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    title="Sales by Region"
)

st.plotly_chart(fig2)


# Monthly Trend

monthly_sales = (
    filtered_df.groupby("Month")["Sales"]
    .sum()
    .reset_index()
)

fig3 = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    title="Monthly Sales Trend"
)

st.plotly_chart(fig3)
