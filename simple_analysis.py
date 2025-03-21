# Import required libraries
import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, avg
import matplotlib.pyplot as plt
import pandas as pd

# Create a Spark session
spark = SparkSession.builder \
    .appName("Simple Sales Analysis") \
    .getOrCreate()

# Load the sales data
print("\n1. Loading sales data...")
sales_df = spark.read.csv("data/sales.csv", header=True, inferSchema=True)

# Show the first few rows of the data
print("\n2. First few rows of our sales data:")
sales_df.show()

# Basic statistics
print("\n3. Basic statistics of our sales data:")
sales_df.describe().show()

# Total sales by product
print("\n4. Total sales by product:")
product_sales = sales_df.groupBy("product") \
    .agg(
        sum("quantity").alias("total_quantity"),
        sum("total").alias("total_sales")
    ) \
    .orderBy("product")
product_sales.show()

# Average price by product
print("\n5. Average price by product:")
avg_prices = sales_df.groupBy("product") \
    .agg(avg("price").alias("average_price")) \
    .orderBy("product")
avg_prices.show()

# Create a simple visualization
print("\n6. Creating a visualization of total sales by product...")
# Convert Spark DataFrame to Pandas for visualization
product_sales_pd = product_sales.toPandas()

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(product_sales_pd['product'], product_sales_pd['total_sales'])
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('data/sales_by_product.png')
plt.close()

print("\nAnalysis complete! Check 'data/sales_by_product.png' for the visualization.")

# Stop the Spark session
spark.stop() 