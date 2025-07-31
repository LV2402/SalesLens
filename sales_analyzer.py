import pandas as pd

# Define the path to your CSV file
csv_file_path = 'sales_data.csv'

# --- 1. Load the data ---
try:
    df = pd.read_csv(csv_file_path)
    print("Data loaded successfully!")
except FileNotFoundError:
    print(f"Error: The file '{csv_file_path}' was not found. Please ensure it's in the same directory as the script.")
    exit() # Exit the script if the file isn't found
except Exception as e:
    print(f"An error occurred while loading the file: {e}")
    exit()

print("\n--- Initial Data Inspection ---")

# --- 2. Display the first few rows ---
print("\nHead of the DataFrame:")
print(df.head())

# --- 3. Display the last few rows ---
print("\nTail of the DataFrame:")
print(df.tail())

# --- 4. Get a concise summary of the DataFrame ---
# This includes data types and non-null values
print("\nInfo about the DataFrame:")
df.info()

# --- 5. Get descriptive statistics for numerical columns ---
print("\nDescriptive Statistics:")
print(df.describe())

# --- 6. Check for missing values ---
print("\nMissing Values per Column:")
print(df.isnull().sum())

# --- 7. Check for unique values in categorical columns (optional, but good practice) ---
print("\nUnique values in 'Category':", df['Category'].unique())
print("Unique values in 'Region':", df['Region'].unique())
print("Unique values in 'CustomerSegment':", df['CustomerSegment'].unique())

# ... (previous code for loading and initial inspection) ...

print("\n--- Data Cleaning and Transformation ---")

# --- 1. Handle missing values in 'Quantity' ---
# We'll fill missing 'Quantity' values with the median.
# The median is often preferred over the mean for quantities to avoid non-integer values
# and is less sensitive to outliers.
median_quantity = df['Quantity'].median()
df['Quantity'].fillna(median_quantity, inplace=True)
print(f"\nMissing 'Quantity' values filled with median: {median_quantity}")

# Verify no more missing values in Quantity
print("\nMissing Values after filling Quantity:")
print(df.isnull().sum())


# --- 2. Convert 'Quantity' to integer type ---
# Since quantity should be a whole number, convert its type.
df['Quantity'] = df['Quantity'].astype(int)
print("\n'Quantity' column converted to integer type.")


# --- 3. Convert 'SaleDate' to datetime objects ---
# This is crucial for time-based analysis later.
df['SaleDate'] = pd.to_datetime(df['SaleDate'])
print("\n'SaleDate' column converted to datetime type.")


# --- 4. Feature Engineering: Calculate 'Revenue' ---
# Revenue = Quantity * UnitPrice
df['Revenue'] = df['Quantity'] * df['UnitPrice']
print("\n'Revenue' column calculated (Quantity * UnitPrice).")


# --- 5. Display the DataFrame after cleaning and transformation ---
print("\nDataFrame after Cleaning and Transformation (first 5 rows):")
print(df.head())

# Verify data types after transformation
print("\nInfo about the DataFrame after transformations:")
df.info()

# ... (previous code for loading, initial inspection, cleaning, and transformation) ...

print("\n--- Data Aggregation and Analysis ---")

# --- 1. Top 5 Products by Revenue ---
print("\nTop 5 Products by Total Revenue:")
top_products_revenue = df.groupby('ProductName')['Revenue'].sum().nlargest(5)
print(top_products_revenue)

# --- 2. Total Revenue by Category ---
print("\nTotal Revenue by Category:")
revenue_by_category = df.groupby('Category')['Revenue'].sum().sort_values(ascending=False)
print(revenue_by_category)

# --- 3. Total Sales (Quantity) by Category ---
print("\nTotal Sales (Quantity) by Category:")
sales_by_category = df.groupby('Category')['Quantity'].sum().sort_values(ascending=False)
print(sales_by_category)

# --- 4. Total Revenue by Region ---
print("\nTotal Revenue by Region:")
revenue_by_region = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
print(revenue_by_region)

# --- 5. Monthly Sales Trends (using SaleDate) ---
# First, extract the month and year from SaleDate
df['SaleMonth'] = df['SaleDate'].dt.to_period('M') # 'M' for month
print("\nMonthly Sales Trends (Total Revenue):")
monthly_revenue = df.groupby('SaleMonth')['Revenue'].sum().sort_index()
print(monthly_revenue)

# --- 6. Sales by Customer Segment ---
print("\nTotal Revenue by Customer Segment:")
revenue_by_segment = df.groupby('CustomerSegment')['Revenue'].sum().sort_values(ascending=False)
print(revenue_by_segment)


print("\n--- Analysis Complete ---")

# ... (previous code for loading, initial inspection, cleaning, transformation, and aggregation) ...

# --- 7. (Optional) Data Visualization ---
import matplotlib.pyplot as plt
import seaborn as sns

print("\n--- Generating Visualizations ---")

# Set a style for better aesthetics
sns.set_style("whitegrid")

# --- Plot 1: Top 5 Products by Revenue (Bar Chart) ---
plt.figure(figsize=(10, 6))
sns.barplot(x=top_products_revenue.index, y=top_products_revenue.values, palette='viridis')
plt.title('Top 5 Products by Total Revenue')
plt.xlabel('Product Name')
plt.ylabel('Total Revenue ($)')
plt.xticks(rotation=45, ha='right') # Rotate labels for better readability
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.savefig('top_products_revenue.png') # Save the plot as an image
print("Saved 'top_products_revenue.png'")
# plt.show() # Uncomment to display the plot immediately (closes after you close it)


# --- Plot 2: Total Revenue by Category (Bar Chart) ---
plt.figure(figsize=(8, 5))
sns.barplot(x=revenue_by_category.index, y=revenue_by_category.values, palette='mako')
plt.title('Total Revenue by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Revenue ($)')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig('revenue_by_category.png')
print("Saved 'revenue_by_category.png'")
# plt.show()


# --- Plot 3: Monthly Sales Trend (Line Plot) ---
# Convert SaleMonth Period to string for plotting if necessary, or let matplotlib handle it
monthly_revenue_plot = monthly_revenue.reset_index()
monthly_revenue_plot['SaleMonth'] = monthly_revenue_plot['SaleMonth'].astype(str) # Convert Period to string for plotting x-axis
plt.figure(figsize=(10, 5))
sns.lineplot(x='SaleMonth', y='Revenue', data=monthly_revenue_plot, marker='o')
plt.title('Monthly Sales Trend (Total Revenue)')
plt.xlabel('Month')
plt.ylabel('Total Revenue ($)')
plt.tight_layout()
plt.savefig('monthly_sales_trend.png')
print("Saved 'monthly_sales_trend.png'")
# plt.show()


# --- Plot 4: Revenue by Customer Segment (Pie Chart) ---
plt.figure(figsize=(7, 7))
plt.pie(revenue_by_segment, labels=revenue_by_segment.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
plt.title('Revenue Distribution by Customer Segment')
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.savefig('revenue_by_customer_segment.png')
print("Saved 'revenue_by_customer_segment.png'")
# plt.show()


# IMPORTANT: If you want to see the plots immediately when the script runs,
# uncomment the `plt.show()` line after each `plt.savefig()` command.
# Otherwise, the plots will only be saved as files in your project directory.
# If you run in an environment like Jupyter Notebook or VS Code with interactive plots,
# plt.show() will display them. For a simple command line execution,
# it might pop up windows that you need to close.
# If using `plt.show()`, it's usually best to have one at the very end to show all plots,
# or one after each plot saving if you want them to appear sequentially.