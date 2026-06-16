# Store Database & Analytics Project

 📌 Project Overview
This project demonstrates the creation of a relational database for a retail store. It showcases the ability to structure data, handle inventory control data types, and use advanced SQL aggregate functions to deliver business-critical statistics.

🛠️ Tech Stack
* **Language:** SQL (Compatible with PostgreSQL, MySQL, SQLite)

 📊 Database Queries & Insights

 1. Inventory Sorted by Price
```sql
SELECT item_name, category, price, stock_quantity
FROM products
ORDER BY price DESC;

2. Business Statistics Generated
SELECT 
    COUNT(*) AS total_unique_items,
    SUM(stock_quantity) AS total_items_in_stock,
    ROUND(AVG(price), 2) AS average_product_price,
    MAX(price) AS most_expensive_item,
    MIN(price) AS cheapest_item
FROM products;


Output Results:

Total Product Variety: 8 unique items
Total Physical Inventory: 495 items in stock
Average Item Price: $91.31
Price Range: $19.99 (Cheapest) to $199.99 (Most Expensive)
