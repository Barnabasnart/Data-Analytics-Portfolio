-- 1. Create the store database table
CREATE TABLE products (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2),
    stock_quantity INT,
    rating DECIMAL(3, 1)
);

-- 2. Insert mock inventory data
INSERT INTO products (item_id, item_name, category, price, stock_quantity, rating) VALUES
(1, 'Wireless Headphones', 'Electronics', 89.99, 45, 4.5),
(2, 'Mechanical Keyboard', 'Electronics', 129.99, 20, 4.7),
(3, 'Leather Wallet', 'Accessories', 45.00, 120, 4.2),
(4, 'Running Shoes', 'Apparel', 110.00, 35, 4.6),
(5, 'Smart Watch', 'Electronics', 199.99, 15, 4.0),
(6, 'Denim Jacket', 'Apparel', 75.50, 60, 4.4),
(7, 'Cotton T-Shirt', 'Apparel', 19.99, 200, 4.1),
(8, 'Bluetooth Speaker', 'Electronics', 59.99, 0, 4.3);



SELECT 
    item_name, 
    category, 
    price, 
    stock_quantity
FROM products
ORDER BY price DESC;



SELECT 
    COUNT(*) AS total_unique_items,                  -- Stat 1: Total Product Variety
    SUM(stock_quantity) AS total_items_in_stock,      -- Stat 2: Total Physical Inventory
    ROUND(AVG(price), 2) AS average_product_price,    -- Stat 3: Average Item Price
    MAX(price) AS most_expensive_item,                -- Stat 4: Highest Price Point
    MIN(price) AS cheapest_item                       -- Stat 5: Lowest Price Point
FROM products;