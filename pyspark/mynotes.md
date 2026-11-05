- https://github.com/kevinschaich/pyspark-cheatsheet

## 1. Initialize SparkSession
```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder \
    .appName("PySparkCheatSheet") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()

```

## 2. Reading & Writing Data

```python
# Read CSV, JSON, Parquet, Delta
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("path/to/file.csv")

# Or direct read methods
df = spark.read.parquet("path/to/data.parquet")

# Write DataFrame
df.write.mode("overwrite").parquet("path/to/output.parquet")
df.write.mode("append").option("header", "true").csv("path/to/output.csv")
```

## 3. Basic DataFrame Inspection & Preview

```python
df.show(5)               # Display top N rows
df.printSchema()         # Print column data types & nullability
df.columns               # List of column names
df.count()               # Total row count
df.describe().show()     # Summary stats (mean, stddev, min, max)
```

## 4. Selecting & Managing Columns

```python
from pyspark.sql.functions import col, lit, expr

# Select columns
df.select("name", "age")
df.select(col("name"), (col("age") + 1).alias("next_age"))

# Add or replace a column
df = df.withColumn("age_plus_10", col("age") + 10)
df = df.withColumn("constant_col", lit("US"))

# Rename columns
df = df.withColumnRenamed("old_name", "new_name")

# Drop columns
df = df.drop("age_plus_10")
```

## 5. Filtering Rows
```python
# Using filter() or where()
df.filter(col("age") > 30)
df.where((col("age") > 30) & (col("department") == "Engineering"))
df.filter(col("name").isin(["Alice", "Bob"]))
df.filter(col("email").isNull())
df.filter(col("email").isNotNull())
```

## 6. Grouping & Aggregations
- Use groupBy() paired with aggregation functions like count, sum, avg, min, and max to summarize data.

## 7. Joins & Broadcast Joins
- Combine DataFrames using standard join types (inner, left, outer, etc.) or optimize joins with small datasets via broadcast().

## 8. Handling Nulls & Duplicates
- Clean data using dropna() for missing values, fillna() for imputation, and dropDuplicates() for deduplication.


## 9. Window Functions
- Perform calculations across related rows using Window.partitionBy() combined with functions like rank(), row_number(), and lag().
