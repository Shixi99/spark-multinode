from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, round as spark_round
import random

# Initialize Spark session
spark = SparkSession.builder \
    .appName("SalesDataAggregation") \
    .getOrCreate()

# Step 1: Generate 2 Million Sales Data Entries
def generate_sales_data(num_rows):
    data = []
    for i in range(num_rows):
        # Simulating data
        order_id = i + 1
        product_id = random.randint(1, 1000)  # Random product IDs between 1 and 1000
        category = random.choice(['Electronics', 'Clothing', 'Home', 'Books', 'Toys'])
        price = round(random.uniform(5.0, 500.0), 2)  # Use Python's round function
        quantity = random.randint(1, 10)  # Quantity between 1 and 10
        total_price = round(price * quantity, 2)

        # Append row as a tuple
        data.append((order_id, product_id, category, price, quantity, total_price))
    
    return data

# Number of rows to generate
num_rows = 500000

# Generate the data
sales_data = generate_sales_data(num_rows)

# Create DataFrame
columns = ['order_id', 'product_id', 'category', 'price', 'quantity', 'total_price']
sales_df = spark.createDataFrame(sales_data, columns)

# Step 2: Perform Aggregation - Sum total sales by category and product_id
aggregated_sales_df = sales_df.groupBy("category", "product_id") \
    .agg(
        sum("quantity").alias("total_quantity_sold"),
        spark_round(sum("total_price"), 2).alias("total_sales_value")  # Use PySpark's round function on columns
    )

# Step 3: Write Aggregated Data to CSV
output_path = "/opt/spark/data/results/sales_aggregated.csv"
aggregated_sales_df.write.mode("overwrite").csv(output_path, header=True)

# Stop Spark session
spark.stop()
