# E-Commerce Sales Analysis

## Project Overview

This project analyzes a sample e-commerce sales dataset using Python and Pandas.

The goal is to understand sales performance, customer behavior, product performance, payment methods, and monthly revenue trends through data analysis and visualization.

## Objectives

- Analyze overall sales and revenue
- Identify high-revenue products and categories
- Compare sales performance across cities
- Analyze monthly revenue trends
- Identify top customers by revenue
- Analyze revenue by payment method
- Compare product sales volume with revenue
- Perform basic data quality checks

## Dataset

The project uses a sample e-commerce dataset created for portfolio and learning purposes.

The dataset contains the following fields:

- Order_ID
- Date
- Customer_ID
- Product
- Category
- Quantity
- Unit_Price
- City
- Payment_Method

## Tools and Technologies

- Python
- Pandas
- Matplotlib
- VS Code
- GitHub

## Analysis Performed

### 1. Revenue Analysis

Revenue was calculated using:

Revenue = Quantity × Unit Price

### 2. Category Analysis

Revenue was grouped by product category to understand category-level performance.

### 3. City Analysis

Revenue was analyzed across different cities.

### 4. Product Analysis

Products were analyzed based on both:

- Total revenue generated
- Total quantity sold

### 5. Monthly Revenue Analysis

Revenue was analyzed across January, February, and March 2026 to identify the monthly trend.

### 6. Payment Method Analysis

Revenue was compared across:

- Card
- UPI
- Cash

### 7. Customer Analysis

Customers were analyzed based on:

- Total revenue generated
- Number of orders
- Top 5 customers by revenue

### 8. Data Quality Check

The dataset was checked for:

- Missing values
- Duplicate rows
- Data types

No missing values or duplicate rows were found in the sample dataset.

## Key Findings

- Total revenue generated was ₹315,745.
- The dataset contains 24 orders.
- Total quantity sold was 137 units.
- Average order value was approximately ₹13,156.
- Electronics generated the highest category revenue of ₹251,050.
- Revenue increased from ₹90,800 in January to ₹118,770 in March 2026.
- Laptop generated the highest product revenue of ₹175,000.
- Pen had the highest quantity sold at 75 units.
- Card payments generated ₹160,500 in recorded revenue.
- The highest-revenue customer in the dataset generated ₹62,000.

## Visualizations

The project includes visualizations for:

- Monthly Revenue
- Revenue by Category
- Revenue by City
- Revenue by Payment Method
- Revenue by Product
- Top 5 Customers by Revenue
- Best-Selling Products by Quantity

The generated charts are available in the `outputs` folder.

## Project Structure

```text
Ecommerce_Sales_Analysis/
│
├── data/
│   └── sales_data.csv
│
├── outputs/
│   ├── monthly_revenue.png
│   ├── category_revenue.png
│   ├── city_revenue.png
│   ├── payment_revenue.png
│   ├── top_customers_revenue.png
│   ├── product_revenue.png
│   └── best_selling_products.png
│
├── main.py
├── requirements.txt
└── README.md