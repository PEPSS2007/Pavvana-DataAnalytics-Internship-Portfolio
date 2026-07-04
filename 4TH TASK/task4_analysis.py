import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# ======================
# KPI SUMMARY
# ======================
print("===== KPI SUMMARY =====")
print("Total Sales:", df["Total_Sales"].sum())
print("Total Orders:", df["Order_ID"].nunique())
print("Total Customers:", df["Customer_ID"].nunique())
print("Average Order Value:", df["Total_Sales"].mean())
print("Total Quantity:", df["Quantity"].sum())

# ======================
# SALES BY CATEGORY
# ======================
category_sales = df.groupby("Category")["Total_Sales"].sum().sort_values()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.close()

# ======================
# SALES BY GENDER
# ======================
gender_sales = df.groupby("Gender")["Total_Sales"].sum()

plt.figure(figsize=(6,6))
gender_sales.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Sales by Gender")
plt.tight_layout()
plt.savefig("sales_by_gender.png")
plt.close()

# ======================
# TOP 10 PRODUCTS
# ======================
top_products = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Top 10 Products")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("top_products.png")
plt.close()

# ======================
# TOP CITIES
# ======================
top_cities = df.groupby("City")["Total_Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_cities.plot(kind="bar")
plt.title("Top Cities")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("top_cities.png")
plt.close()

# ======================
# MONTHLY SALES
# ======================
monthly_sales = df.groupby(df["Order_Date"].dt.month)["Total_Sales"].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.close()

print("All charts saved successfully!")
from scipy.stats import ttest_ind

# Separate sales by gender
male_sales = df[df["Gender"] == "Male"]["Total_Sales"]
female_sales = df[df["Gender"] == "Female"]["Total_Sales"]

# Perform Independent T-Test
t_stat, p_value = ttest_ind(male_sales, female_sales, nan_policy="omit")

print("\n===== HYPOTHESIS TEST =====")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print("Conclusion: Reject the Null Hypothesis")
    print("There is a statistically significant difference in spending between male and female customers.")
else:
    print("Conclusion: Fail to Reject the Null Hypothesis")
    print("There is NO statistically significant difference in spending between male and female customers.")