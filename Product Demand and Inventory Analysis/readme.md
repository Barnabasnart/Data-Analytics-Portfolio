# 📦 Product Demand and Inventory Analysis — Power BI & Supply Chain Dashboard

An interactive Power BI dashboard analyzing product demand patterns, stock availability, supplier lead times, and inventory turnover across multiple warehouse locations.

## 📌 Project Overview
This project processes inventory telemetry, order fulfillments, and stock level logs to help supply chain managers balance product availability against holding costs. It provides actionable visibility into stockout risks, safety stock buffers, reorder triggers, and regional demand dynamics.

*Business Objective:* Evaluate demand patterns and inventory performance to optimize stock turnover, reduce carrying costs, and prevent inventory stockouts across fulfillment hubs.

## 🎯 Key KPIs
* **Total Inventory Units** — Aggregate stock count across all active product categories and warehouse locations.
* **Total Carrying Value** — Total financial capital tied up in current inventory holdings.
* **Average Reorder Lead Time** — Mean days required for suppliers to replenish stock levels.
* **Stockout Risk Rate** — Percentage of inventory lines currently below safety stock thresholds.

## 📊 Dashboards

### 1. Overview Analysis
* Dynamic **Measure Selector** (disconnected table) to toggle between Total Demand Units, Inventory Carrying Value, and Stockout Risk Rates.
* Category breakdown map and performance metrics across top product lines.
* Global slicers for **Warehouse Location**, **Product Category**, and **Supplier Status**.
* Dynamic visual headers that update automatically based on the selected metric.

### 2. Inventory & Stock Turnover
* **Stock Level vs. Reorder Point Matrix** — Highlighting SKU lines requiring immediate replenishment.
* **Supplier Lead Time Efficiency** — Comparative analysis evaluating vendor delivery performance against fulfillment SLAs.
* Demand volatility trends tracking peak sales periods against inventory depletion rates.

### 3. Details Tab
* Granular records matrix tracking individual SKU logs, stock levels, reorder quantities, and warehouse locations.
* Drill-through capability for localized product-level diagnostic exploration.

## 🛠️ Tools & Techniques Used
* **Power BI & DAX** — Advanced data modeling, custom measures, and interactive reporting.
* **Disconnected Tables** — Enables dynamic switching of metrics across key visuals.
* **Bookmarks & Buttons** — Interactive UX features including view toggles and filter reset options.
* **Conditional Formatting** — Highlighting reorder alerts, low-stock warnings, and excess holding costs.

## 📷 Screenshots



## 🚀 Key Insights & Outcomes
* **Stock Optimization:** Identified critical fast-moving SKU lines reaching reorder points ahead of standard lead times, preventing potential stockouts.
* **Holding Cost Reduction:** Isolated slow-moving product categories tieing up excessive working capital, providing actionable opportunities for promotional bundling or inventory clearance.
* **Supplier SLA Performance:** Highlighted supplier lead-time variances to negotiate improved delivery windows and optimize safety stock parameters across fulfillment centers.

## 📬 Contact
Built by **Barnabas Nartey** — Data Analyst  
Feel free to connect or reach out with feedback!
