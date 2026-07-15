 📊 Nationwide Telecom Infrastructure & Performance Analytics (Ghana)

 📌 Project Overview
This project delivers an end-to-end data engineering and business intelligence solution analyzing **1 year of network telemetry data** (August 2025 - July 2026) across all **16 regions of Ghana**. 

By simulating massive, real-world network loads, infrastructure types (4G, 5G, Fiber), and operational incidents, this project answers critical executive questions regarding service quality (QoS), capacity planning, and maintenance turnaround efficiency.

---
## 🛠️ Tech Stack & Architecture
* **Data Simulation & Pipeline:** Python (`pandas`, `numpy`, `sqlalchemy`, `pymysql`)
* **Database & Warehousing:** MySQL Server (Relational star-schema modeling, DDL scripting, performance-optimized SQL Views)
* **Business Intelligence:** Power BI Desktop, DAX (Data Analysis Expressions)

---

## 📐 Data Model & Database Architecture
The data is structured as an optimized **Star Schema** to ensure high-performance reporting:
* **`Base_Stations` (Dimension):** Tracks 100 cell towers, hardware capacities, technology types, and regional locations across Ghana.
* **`Performance_Logs` (Fact):** 36,500 rows capturing daily call counts, data volume (GB), and dropped sessions per tower.
* **`Outage_Incidents` (Fact):** 2,500 records logging unplanned network downtime events, root causes, and severity metrics.

**An optimized database SQL view (`v_ghana_network_performance`) was written to handle resource-heavy multi-table joins at the database layer, preserving Power BI memory footprint and dashboard interactivity.**

---

## 💡 Key Business Insights Discovered
1. **SLA Adherence:** The nationwide Call Drop Rate settles at **0.804%**, successfully meeting the global telecom benchmark threshold of `< 1.0%`.
2. **Operational Bottleneck:** Deep-dive analysis uncovered an optimization flaw in field maintenance routines: **Critical incidents have an MTTR of 5.0 hours**, while **Minor incidents take 5.3 hours**. Operations require an automated high-severity triage update.
3. **Geographical Constraints:** The **Eastern and Western regions** are the country’s primary quality bottleneck zones, accounting for over **2.2 Million aggregate dropped calls**, independent of raw site capacity configurations.

---


---
**Developed by Barnabas Nartey | Data Analyst & Telecommunication Engineering Specialist**
