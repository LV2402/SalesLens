# SalesLens: Simple CSV Data Processor & Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-v1.x%2B-orange?style=for-the-badge&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-v3.x%2B-brightgreen?style=for-the-badge&logo=matplotlib)
![Seaborn](https://img.shields.io/badge/Seaborn-v0.x%2B-purple?style=for-the-badge&logo=seaborn)

---

## Overview

**SalesLens** is a foundational data analysis project developed in Python, designed to process, clean, transform, and analyze sales data from a CSV file. It demonstrates a practical application of data manipulation and aggregation techniques using the Pandas library, akin to performing SQL-like operations on a tabular dataset. The project aims to extract meaningful business insights from raw sales figures, such as identifying top-performing products, understanding sales trends over time, and breaking down revenue by various dimensions like category and region. It also visualizes these insights to enhance understanding.

---

## Key Features & Components

The project follows a typical data analysis workflow, broken down into distinct stages:

1.  ### Data Loading and Initial Inspection
    * Loads raw sales data from `sales_data.csv` into a Pandas DataFrame.
    * Performs initial checks using `head()`, `tail()`, `info()`, `describe()`, and `isnull().sum()` to understand data structure, types, and identify missing values.

2.  ### Data Cleaning and Transformation
    * **Handles Missing Values:** Imputes missing 'Quantity' values with the median to maintain data integrity and consistency.
    * **Type Conversion:** Converts 'Quantity' from `float` to `int` and 'SaleDate' from `object` (string) to `datetime` for accurate numerical and time-based analysis.
    * **Feature Engineering:** Creates a new 'Revenue' column by multiplying 'Quantity' and 'UnitPrice', a crucial metric for sales analysis.

3.  ### Data Aggregation and Analysis
    * Summarizes cleaned data to extract actionable business insights.
    * Identifies **Top 5 Products by Total Revenue**.
    * Calculates **Total Revenue and Quantity Sold by Product Category**.
    * Determines **Total Revenue by Sales Region**.
    * Analyzes **Monthly Sales Trends** (though the provided data is for one month, the code supports multi-month trends).
    * Breaks down **Total Revenue by Customer Segment**.

4.  ### Data Visualization
    * Generates informative plots using Matplotlib and Seaborn to visualize key sales metrics.
    * Visualizations include:
        * Bar Chart: Top 5 Products by Revenue
        * Bar Chart: Total Revenue by Product Category
        * Line Plot: Monthly Sales Trend (Total Revenue)
        * Pie Chart: Revenue Distribution by Customer Segment
    * All plots are saved as `.png` image files in the project directory.

---

## Technologies Used

* **Python 3.x**
* **Pandas:** For data manipulation and analysis.
* **Matplotlib:** For creating static visualizations.
* **Seaborn:** For enhancing the aesthetics and statistical plots.

---

## Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

* Python 3.8+ installed on your system.
* `pip` (Python package installer)

### Installation

1.  **Clone the Repository (if applicable) or create a new folder:**
    ```bash
    mkdir CSV_Data_Processor
    cd CSV_Data_Processor
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Required Libraries:**
    ```bash
    pip install pandas matplotlib seaborn
    ```

### Data Preparation

1.  **Create the CSV File:**
    Inside your `CSV_Data_Processor` folder, create a file named `sales_data.csv` and paste the following fictional sales data into it:

    ```csv
    OrderID,ProductID,ProductName,Category,Quantity,UnitPrice,SaleDate,Region,CustomerSegment
    1001,P001,Laptop Pro,Electronics,2,1200.00,2023-01-05,North,Consumer
    1002,P003,Mechanical Keyboard,Electronics,1,150.00,2023-01-06,South,Corporate
    1003,P002,Wireless Mouse,Electronics,3,25.00,2023-01-07,East,Consumer
    1004,P001,Laptop Pro,Electronics,1,1200.00,2023-01-08,West,Consumer
    1005,P004,Ergonomic Chair,Office Furniture,1,300.00,2023-01-09,North,Corporate
    1006,P005,Desk Lamp,Office Furniture,2,45.00,2023-01-10,South,Consumer
    1007,P001,Laptop Pro,Electronics,1,1200.00,2023-01-11,East,Corporate
    1008,P006,Coffee Maker,Home Appliances,1,75.00,2023-01-12,West,Consumer
    1009,P003,Mechanical Keyboard,Electronics,2,150.00,2023-01-13,North,Consumer
    1010,P007,Smartphone X,Electronics,1,800.00,2023-01-14,South,Consumer
    1011,P002,Wireless Mouse,Electronics,NaN,25.00,2023-01-15,East,Corporate
    1012,P005,Desk Lamp,Office Furniture,1,45.00,2023-01-16,West,Consumer
    1013,P004,Ergonomic Chair,Office Furniture,1,300.00,2023-01-17,North,Corporate
    1014,P001,Laptop Pro,Electronics,1,1200.00,2023-01-18,South,Consumer
    1015,P008,External SSD,Electronics,1,90.00,2023-01-19,East,Consumer
    1016,P003,Mechanical Keyboard,Electronics,NaN,150.00,2023-01-20,West,Corporate
    1017,P001,Laptop Pro,Electronics,2,1200.00,2023-01-21,North,Consumer
    1018,P009,Smart Watch,Electronics,1,250.00,2023-01-22,South,Consumer
    1019,P010,Bluetooth Speaker,Electronics,3,60.00,2023-01-23,East,Corporate
    1020,P002,Wireless Mouse,Electronics,2,25.00,2023-01-24,West,Consumer
    1021,P007,Smartphone X,Electronics,1,800.00,2023-01-25,North,Consumer
    1022,P006,Coffee Maker,Home Appliances,1,75.00,2023-01-26,South,Corporate
    1023,P001,Laptop Pro,Electronics,1,1200.00,2023-01-27,East,Consumer
    1024,P008,External SSD,Electronics,2,90.00,2023-01-28,West,Consumer
    1025,P004,Ergonomic Chair,Office Furniture,1,300.00,2023-01-29,North,Corporate
    ```

### Running the Script

1.  **Save the Python script:**
    Save your Python code (from our previous steps) as `sales_analyzer.py` in the same `CSV_Data_Processor` folder as `sales_data.csv`.

2.  **Run the script from your terminal (with virtual environment activated):**
    ```bash
    python sales_analyzer.py
    ```
    The script will print analysis results to the console and save the generated plots as `.png` files in the same directory.

---

## Key Insights from Analysis

Based on the provided fictional sales data, the **SalesLens** analysis reveals the following insights:

* **Top Product:** "Laptop Pro" is the overwhelming revenue generator, significantly outperforming other products.
* **Dominant Category:** "Electronics" is the leading category by a large margin in terms of both total revenue and units sold.
* **Regional Performance:** The "North" region generates the highest revenue.
* **Customer Segment:** The "Consumer" segment contributes significantly more revenue than the "Corporate" segment.
* **Sales Trends:** All sales in this dataset occurred within January 2023.

---

## Visualizations

The `sales_analyzer.py` script generates and saves the following visualizations to your project directory, offering a quick visual summary of the analysis:

* `top_products_revenue.png`
* `revenue_by_category.png`
* `monthly_sales_trend.png`
* `revenue_by_customer_segment.png`

*(You can uncomment `plt.show()` lines in the script if you want to see the plots pop up interactively when running the script.)*

---

## Future Enhancements

Possible improvements and extensions for this project include:

* **More Robust Error Handling:** Add more comprehensive error checks for data loading and processing.
* **Command Line Arguments:** Allow specifying input/output file paths via command line arguments.
* **Interactive Visualizations:** Integrate libraries like Plotly or Bokeh for interactive dashboards.
* **Advanced Analysis:** Implement more complex statistical analysis, forecasting, or customer segmentation (e.g., RFM analysis).
* **Data Validation:** Add checks for data integrity (e.g., `Quantity` or `UnitPrice` cannot be negative).
* **Reporting:** Generate a summary report in a different format (e.g., PDF, HTML).

---

## Author

**[LV]**
* GitHub: [LV2402]([https://github.com/LV2402])

---
