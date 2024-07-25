import pandas as pd
import pyspark
from pyspark.sql import SparkSession, functions as F
from tabulate import tabulate

# Initialize Spark session
spark = SparkSession.builder.master("local").appName("Standardize").getOrCreate()

# Sample DataFrame for testing
data = {
    'A': [4560000, 340, 23560],
    'B': ['val1', 'val2', 'val3'],
    'C': [123.0, 456.0, 789.0]
}

pdf = pd.DataFrame(data)

# Convert Pandas DataFrame to Spark DataFrame
df = spark.createDataFrame(pdf)

# Sample column mapping for testing
column_mapping = {
    'new_A': 'A',
    'new_B': ['B', 'C'],
    'new_static': '$static_value'
}

class Standardizer:
    def standardize_columns(self, df, column_mapping):
        for new_col, old_col in column_mapping.items():
            if isinstance(old_col, str) and old_col.startswith('$'):
                static_value = old_col.lstrip('$')
                df = df.withColumn(new_col, F.lit(static_value))
            elif isinstance(old_col, list):
                df = df.withColumn(new_col, F.concat_ws('_', *[df[col] for col in old_col]))
            else:
                df = df.withColumn(new_col, df[old_col].alias(new_col) if old_col != new_col else df[old_col])

        # Convert all columns to string type
        df = df.select(*(F.col(col).cast("string").alias(col) for col in df.columns))

        # Remove trailing .0 from any strings
        df = df.select(*(F.regexp_replace(F.col(col), r'\.0$', '').alias(col) for col in df.columns))

        select_columns = [new_col for new_col in column_mapping.keys()]
        return df.select(*select_columns)

def standardize_rows(member_sf_df):
    # List of columns to exclude from conversion
    exclusion_list = ['ROW_NUMBER']

    # Apply conversion only to columns not in the exclusion list
    for col in member_sf_df.columns:
        if col not in exclusion_list:
            # Use vectorized string operations to check and replace '.0' suffix
            member_sf_df[col] = member_sf_df[col].astype(str)
            # Remove the .0 suffix for values that appear as floats
            member_sf_df[col] = member_sf_df[col].str.replace(r'\.0$', '', regex=True)

    return member_sf_df


# Initialize Standardizer instance
standardizer = Standardizer()

# Apply the standardize_columns method
standardized_df = standardizer.standardize_columns(df, column_mapping)

# Convert Spark DataFrame to Pandas DataFrame for displaying
standardized_pdf = standardized_df.toPandas()

standardized_pdf = standardize_rows(standardized_pdf)


# Display the standardized DataFrame
print(tabulate(standardized_pdf, headers='keys', tablefmt='psql'))
