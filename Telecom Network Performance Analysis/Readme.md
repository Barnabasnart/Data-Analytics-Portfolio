# 📊 Telecom Network Performance Analysis — Power BI & SQL

An end-to-end data engineering and business intelligence solution analyzing 1 year of network telemetry data across all 16 regions of Ghana to monitor service quality, capacity planning, and maintenance turnaround efficiency.

## 📌 Project Overview
This project simulates real-world network loads, infrastructure types (4G, 5G, Fiber), and operational outage incidents. It provides telecom executives and network operations teams with actionable insights to track Quality of Service (QoS) metrics, reduce downtime, and meet service-level agreements (SLAs).

*Business Objective:* Evaluate network performance, identify outage bottlenecks, and optimize field maintenance response times across cellular tower infrastructure in Ghana.

## 🎯 Key KPIs
* **Call Drop Rate** — Percentage of dropped calls nationwide (Benchmark: < 1.0%).
* **Mean Time to Repair (MTTR)** — Average hours required to resolve network outage incidents.
* **Total Data Volume** — Aggregate data throughput (GB) processed across cell towers.
* **Active Base Stations** — Total number of monitored 4G, 5G, and Fiber cell sites.

## 📊 Dashboards

### 1. Overview Analysis
* Dynamic **Measure Selector** (disconnected table) to toggle between Call Drop Rate, Total Data Volume, and Incident Counts.
* Regional breakdown map and performance cards across all **16 Regions of Ghana**.
* Technology type slicers (**4G, 5G, Fiber**) and site severity status indicators.
* Dynamic chart titles that update based on selected telemetry metrics.

### 2. Time & Operational Analysis
* **MTTR Breakdown** — Maintenance resolution times evaluated by incident severity level.
* **Outage Incident Trends** — Distribution of unplanned network downtime over 10-minute and daily time intervals.
* Peak load area charts comparing weekday vs. weekend data traffic spikes.

### 3. Details Tab
* Granular records matrix tracking individual tower logs and incident IDs.
* Drill-through capability for localized site-level diagnostic exploration.

## 🛠️ Tools & Techniques Used
* **Python** (`pandas`, `numpy`, `sqlalchemy`, `pymysql`) — Synthetic data pipeline & telemetry generation.
* **MySQL Server** — Relational star-schema warehouse and performance-optimized SQL Views (`v_ghana_network_performance`).
* **Power BI & DAX** — Data modeling, custom measures, and interactive reporting.
* **Disconnected Tables** — Enables dynamic switching of metrics across primary visuals.
* **Bookmarks & Buttons** — User interactive features including filter resets and detail views.

## 📷 Screenshots

<img src="Telecom Network Performance Dashboard.jpg" alt="Telecom Network Performance Dashboard" width="100%" />

## 🚀 Key Insights & Outcomes
* **SLA Adherence:** Maintained a nationwide Call Drop Rate of **0.804%**, remaining well below the 1.0% global standard limit.
* **Operational Bottleneck:** Identified a triaging delay in field support where critical incidents took **5.0 hours** to resolve compared to **5.3 hours** for minor issues.
* **Regional Bottlenecks:** Discovered that the **Eastern and Western regions** accounted for over **2.2 Million aggregate dropped calls**, highlighting physical coverage gaps rather than tower capacity constraints.

## 📬 Contact
Built by **Barnabas Nartey** — Data Analyst 
Feel free to connect or reach out with feedback!
