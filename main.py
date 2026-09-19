import pandas as pd
import matplotlib.pyplot as plt

def calculate_revenue(data):
    data["Revenue"] = data["Quantity"] * data["Unit_Price"]
    return data

# Load the dataset
data = pd.read_csv("data/sales_data.csv")

# Convert Date column into date format
data["Date"] = pd.to_datetime(data["Date"])

# Create Revenue column
data = calculate_revenue(data)

# First 5 rows
print("First 5 rows:")
print(data.head())

# Revenue for each order
print("\nRevenue for each order:")
print(data[["Order_ID", "Product", "Quantity", "Unit_Price", "Revenue"]])

# Revenue by Category
category_revenue = data.groupby("Category")["Revenue"].sum()

print("\nRevenue by Category:")
print(category_revenue)

# Revenue by City
city_revenue = data.groupby("City")["Revenue"].sum()

print("\nRevenue by City:")
print(city_revenue)

# Revenue by Product
product_revenue = data.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Product:")
print(product_revenue)

# Quantity Sold by Product
product_quantity = data.groupby("Product")["Quantity"].sum().sort_values(ascending=False)

print("\nQuantity Sold by Product:")
print(product_quantity)

# Create Month column
data["Month"] = data["Date"].dt.to_period("M")

# Monthly Revenue
monthly_revenue = data.groupby("Month")["Revenue"].sum()

print("\nMonthly Revenue:")
print(monthly_revenue)

# Monthly Revenue Chart
monthly_revenue = data.groupby("Month")["Revenue"].sum()

plt.figure(figsize=(8, 5))
plt.plot(monthly_revenue.index.astype(str), monthly_revenue.values, marker="o")

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.grid(True)

plt.savefig("outputs/monthly_revenue.png")
plt.show()

# Category Revenue Chart
category_revenue = data.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
plt.bar(category_revenue.index, category_revenue.values)

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (₹)")
plt.grid(axis="y")

plt.savefig("outputs/category_revenue.png")

plt.show()

# City Revenue Chart
city_revenue = data.groupby("City")["Revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
plt.bar(city_revenue.index, city_revenue.values)

plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue (₹)")
plt.grid(axis="y")

plt.savefig("outputs/city_revenue.png")

plt.show()

# Payment Method Analysis
payment_revenue = data.groupby("Payment_Method")["Revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Payment Method:")
print(payment_revenue)

# Payment Method Revenue Chart
plt.figure(figsize=(8, 5))
plt.bar(payment_revenue.index, payment_revenue.values)

plt.title("Revenue by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Revenue (₹)")
plt.grid(axis="y")

plt.savefig("outputs/payment_revenue.png")

plt.show()

# Customer Revenue Analysis
customer_revenue = data.groupby("Customer_ID")["Revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Customer:")
print(customer_revenue)

# Top 5 Customers
top_customers = customer_revenue.head(5)

print("\nTop 5 Customers by Revenue:")
print(top_customers)

# Number of Orders per Customer
customer_orders = data.groupby("Customer_ID")["Order_ID"].count().sort_values(ascending=False)

print("\nNumber of Orders per Customer:")
print(customer_orders)

# Top 5 Customers by Revenue
top_customers = customer_revenue.head(5)

print("\nTop 5 Customers by Revenue:")
print(top_customers)

# Top 5 Customers Revenue Chart
plt.figure(figsize=(8, 5))
plt.bar(top_customers.index, top_customers.values)

plt.title("Top 5 Customers by Revenue")
plt.xlabel("Customer ID")
plt.ylabel("Revenue (₹)")
plt.grid(axis="y")

plt.savefig("outputs/top_customers_revenue.png")

plt.show()

# Top 5 Customers Revenue Chart
plt.figure(figsize=(8, 5))
plt.bar(top_customers.index, top_customers.values)

plt.title("Top 5 Customers by Revenue")
plt.xlabel("Customer ID")
plt.ylabel("Revenue (₹)")
plt.grid(axis="y")

plt.savefig("outputs/top_customers_revenue.png")

plt.show()

# Data Quality Check

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDuplicate Rows:")
print(data.duplicated().sum())

print("\nData Types:")
print(data.dtypes)

# Key Performance Indicators (KPIs)

total_revenue = data["Revenue"].sum()
total_orders = data["Order_ID"].nunique()
total_quantity = data["Quantity"].sum()
average_order_value = total_revenue / total_orders

print("\n========== KEY PERFORMANCE INDICATORS ==========")
print(f"Total Revenue: ₹{total_revenue:,.0f}")
print(f"Total Orders: {total_orders}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Average Order Value: ₹{average_order_value:,.2f}")

# Product Revenue Chart
product_revenue = data.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(product_revenue.index, product_revenue.values)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("outputs/product_revenue.png")

plt.show()

# Best-Selling Products by Quantity
best_selling = data.groupby("Product")["Quantity"].sum().sort_values(ascending=False)

print("\nBest-Selling Products by Quantity:")
print(best_selling)

# Best-Selling Products Chart
best_selling = data.groupby("Product")["Quantity"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(best_selling.index, best_selling.values)

plt.title("Best-Selling Products by Quantity")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("outputs/best_selling_products.png")

plt.show()