# 🚕 Taxi Driver Earnings Tracker — Python Data Pipeline

An end-to-end Python data analysis and visualization pipeline designed to track, audit, and optimize daily taxi driver earnings, operational fuel efficiency, and trip unit economics.

## 📌 Project Overview
This project processes operational ride logs to evaluate daily profitability against target benchmarks, flag high fuel consumption days, and analyze net earnings trends across multiple driving shifts. It provides drivers and fleet managers with structured financial audits to improve operational efficiency.

*Business Objective:* Automate daily driver income auditing, monitor fuel-to-fare ratios, and evaluate trip revenue patterns to maximize net profitability.

## 🎯 Key KPIs
* **Total Net Earnings** — Aggregate driver profit calculated as Total Fares minus Fuel Costs (e.g., **GHS 3,030.00** across sample period).
* **Average Daily Net Earnings** — Mean net revenue earned per driving shift.
* **Average Fare per Trip** — Mean fare revenue generated per completed ride.
* **Fuel Efficiency Flag** — Threshold indicator flagging days where fuel costs exceed **30%** of total gross fares.

## 📊 Analytics Breakdown

### 1. Data Processing & Logic (Python & Pandas)
* **Target Auditing:** Custom control structures evaluating whether net earnings meet or fall below daily income targets.
* **Custom Functions & Lambda Expressions:** Automated calculations for `net_earnings()`, `average_fare_per_trip()`, and dynamic flags for `High Fuel Day` shifts.
* **Array Analytics (NumPy):** Identification of statistical performance bounds, including average earnings and pinpointing the worst-earning shift date and index.

### 2. Operational Insights & Visualizations (Matplotlib)
* **Earnings Trend Line Chart:** Tracking daily net income trajectory across driving dates to evaluate performance consistency.
* **Fares vs. Fuel Cost Bar Chart:** Comparative side-by-side visualization analyzing gross revenue relative to fuel expenditure per shift.
* **Efficiency Audit Filter:** Isolated review matrix highlighting shifts flagged with high fuel overhead.

## 🛠️ Tools & Techniques Used
* **Python 3** — Core language for analytical script execution.
* **Pandas** — Data manipulation, chronological sorting, filtering, and feature engineering.
* **NumPy** — Vectorized statistical computations (mean, min, argmin analysis).
* **Matplotlib** — Data visualization and dual-metric chart rendering.

## 📷 Visualizations



## 🚀 Key Insights & Outcomes
* **Fuel Efficiency Alerts:** Successfully isolated high-overhead shifts where fuel costs consumed over 30% of gross fares, providing targeted days for route optimization.
* **Target Tracking:** Automated daily threshold checks allowing drivers to instantly verify target achievement versus shortfalls.
* **Performance Bounds:** Identified low-earning outlier days to correlate with trip volume drops or high fuel consumption.

## 📬 Contact
Built by **Barnabas Nartey** — Data Analyst  
Feel free to connect or reach out with feedback!
