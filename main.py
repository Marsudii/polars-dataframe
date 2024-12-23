import polars as pl


# Load data unclean.csv
df = pl.read_csv('sample-data/unclean_users_data.csv')

# Remove rows with null values
df_clean = df.drop_nulls()

# Order by column 'name' acsending
df_clean = df_clean.sort('Full Name')


# Generate file clean.csv
df_clean.write_csv('sample-data/clean_users_data.csv')

print("Data cleaning")