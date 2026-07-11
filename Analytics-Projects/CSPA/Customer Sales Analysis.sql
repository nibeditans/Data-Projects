CREATE DATABASE customer_sales_analysis;

SELECT * FROM sales_data_sample;

SELECT ORDER_DATE 
FROM sales_data_sample;

/*
Here, the Order Date is completely messy. 
Let's clean that first.

Formatting dates in MySQL is quite straightforward. 
We can use the DATE_FORMAT() function to format dates in various styles.
			--------------------------
			 DATE_FORMAT(date, format)
			--------------------------
Common Date Formats: 
	- YYYY-MM-DD ('%Y-%m-%d')
	- DD/MM/YYYY ('%d/%m/%Y')
	- Month Day, Year ('%M %d, %Y')
    - Day of Week, Day Month Year ('%W, %d %M %Y')
    
Here, we have to clean and standardize the ORDER_DATE, 
as the formats are MM/DD/YYYY HH:MI and MM-DD-YYYY HH:MI now.
So, let's first create a new column to store the cleaned dates.
*/
ALTER TABLE sales_data_sample 
ADD COLUMN cleaned_order_date DATE;

-- Now, we can convert and update the dates
# Convert dates with format MM/DD/YYYY
UPDATE sales_data_sample
SET cleaned_order_date = STR_TO_DATE(order_date, '%m/%d/%Y %H:%i')
WHERE order_date LIKE '%/%/%';

# Convert dates with format MM-DD-YYYY
UPDATE sales_data_sample
SET cleaned_order_date = STR_TO_DATE(order_date, '%m-%d-%Y %H:%i')
WHERE order_date LIKE '%-%-%';


SELECT order_date, cleaned_order_date 
FROM sales_data_sample;

ALTER TABLE sales_data_sample 
DROP COLUMN ADDRESS_LINE2;

SHOW COLUMNS FROM sales_data_sample;


-- Total Sales per Customer
SELECT customer_name, 
	ROUND(SUM(sales), 2) total_sales
FROM sales_data_sample
GROUP BY customer_name
ORDER BY total_sales DESC;


-- Monthly/Quarterly Sales Trends
# Monthly Sales Trends
SELECT MONTH_ID, 
	ROUND(SUM(SALES), 2) total_sales
FROM sales_data_sample
GROUP BY MONTH_ID
ORDER BY total_sales DESC;

# Quarterly Sales Trends
SELECT QTR_ID, 
	ROUND(SUM(SALES), 2) total_sales
FROM sales_data_sample
GROUP BY QTR_ID
ORDER BY total_sales DESC;

# Yearly Sales Trends
SELECT YEAR_ID, 
	ROUND(SUM(SALES), 2) total_sales
FROM sales_data_sample
GROUP BY YEAR_ID
ORDER BY total_sales DESC;


-- Product Line Analysis
/*
For this, we have to find the Profit first. 
Again, we need Cost values for that. As we don't have
a Cost column in our dataset, I'm assuming cost is 
70% of the unit price. Let's first add a Cost column.
Next, we'll calculate and add the Profit column. And then
we'll do the Product Line Analysis.
*/
ALTER TABLE sales_data_sample 
ADD COLUMN cost DECIMAL(10, 2);

/*
If we do this, we may see warnings as 
"Data truncated for column", because it shouldn't 
exceed its defined precision and scale. But in 
this case, it will. So, let's modify its Data Type 
to DOUBLE to avoid data truncation issues.
*/
ALTER TABLE sales_data_sample 
MODIFY COLUMN cost DOUBLE;

UPDATE sales_data_sample
SET cost = PRICE_EACH * 0.7;

SELECT PRODUCT_LINE, 
	ROUND(cost, 2) total_cost
FROM sales_data_sample;

-- Adding the Profit Column
ALTER TABLE sales_data_sample 
ADD COLUMN profit DOUBLE;

UPDATE sales_data_sample
SET profit = sales - cost;

SELECT PRODUCT_LINE, 
	ROUND(profit, 2) total_profit
FROM sales_data_sample;

-- Which Product Lines are the most profitable?
SELECT PRODUCT_LINE, 
	ROUND(SUM(profit), 2) total_profit
FROM sales_data_sample
GROUP BY PRODUCT_LINE
ORDER BY total_profit DESC;


-- Customer Segmentation
# Frequent vs. Infrequent Purchases
SELECT customer_name, 
	COUNT(ORDER_NUMBER) total_orders
FROM sales_data_sample
GROUP BY customer_name
ORDER BY total_orders DESC;


-- Order Patterns and Seasonality
# Orders by Status
SELECT `status`, 
	COUNT(QUANTITY_ORDERED) total_qty
FROM sales_data_sample
GROUP BY `status`
ORDER BY total_qty DESC;

# Sales Seasonality
ALTER TABLE sales_data_sample
ADD COLUMN day_of_the_week TEXT;

UPDATE sales_data_sample
SET day_of_the_week = DAYNAME(cleaned_order_date);

SELECT day_of_the_week,
	ROUND(SUM(sales), 2) total_sales
FROM sales_data_sample
GROUP BY day_of_the_week
ORDER BY total_sales;


-- Data Integrity Checks
SELECT COUNT(*) FROM sales_data_sample;

SELECT COUNT(DISTINCT ORDER_NUMBER)
FROM sales_data_sample;

SELECT ORDER_NUMBER, COUNT(*) AS entry_count
FROM sales_data_sample
GROUP BY ORDER_NUMBER
HAVING COUNT(*) > 1
ORDER BY entry_count DESC;
/*
In this context, having multiple entries per 
ORDER_NUMBER is expected since each entry represents 
a different product line within the same order. It's a 
common structure in sales and transaction datasets.
*/

# Checking for any Missing Data
SELECT PHONE, 
	COUNTRY, 
    CONTACT_FIRST_NAME
FROM sales_data_sample
WHERE CONTACT_FIRST_NAME IS NULL;
/*
We found out that the columns PHONE, COUNTRY, and 
CONTACT_FIRST_NAME do not have missing entries, 
making our dataset reliable for further analysis.
*/


-- Customer-Level Sales
# Summarizes total sales per customer.
CREATE VIEW customer_sales_summary AS
SELECT 
    CUSTOMER_NAME,
    SUM(SALES) AS total_sales,
    COUNT(ORDER_NUMBER) AS total_orders
FROM sales_data_sample
GROUP BY CUSTOMER_NAME;

SELECT * FROM customer_sales_summary;


-- Monthly Sales Trends
# Summarizes sales by month and year.
CREATE VIEW monthly_sales_trends AS
SELECT 
    YEAR_ID,
    MONTH_ID,
    SUM(SALES) AS total_sales,
    COUNT(ORDER_NUMBER) AS total_orders
FROM sales_data_sample
GROUP BY YEAR_ID, MONTH_ID;

SELECT * FROM monthly_sales_trends;


SELECT ORDER_DATE, cleaned_order_date
FROM csa_data_df_to_db;

SELECT ORDER_DATE, cleaned_order_date
FROM sales_data_sample;






