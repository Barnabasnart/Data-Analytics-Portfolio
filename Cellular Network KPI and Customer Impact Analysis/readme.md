# 📊 Cellular Network KPI & Customer Impact Analysis — Power BI & SQL

An end-to-end data engineering and business intelligence solution analyzing 50,000 telemetry records over a full year (2025) across all **16 regions of Ghana** to evaluate deep radio frequency (RF) performance, infrastructure health, and its direct commercial impact on subscriber churn and revenue.

---

## 📌 Project Overview

This project simulates enterprise-grade cellular network telemetry, combining core radio access performance indicators (RSRP, SINR, Drop Call Rates, and Throughput) with business metrics like **Estimated Revenue Loss (GHS)** and a **Customer Churn Risk Index (%)**. 

* **Business Objective:** Bridge deep RF engineering analytics with executive decision-making to identify network bottlenecks, mitigate customer-impacting degradation, and protect commercial revenue across Ghana's mobile infrastructure.

---

## 🎯 Key KPIs (Executive Dashboard Summary)

* **Avg Churn Risk Index (13.06%)** — Average predictive percentage of subscribers at risk of churning due to poor service quality.
* **Avg CSSR (96.95%)** — Overall reliability percentage for initiating successful voice and data connections.
* **Avg Data Throughput (71.11 Mbps)** — Average user data download speeds across network nodes.
* **Avg Drop Call Rate (2.28%)** — Percentage of prematurely disconnected voice calls nationwide.
* **Avg Packet Loss Rate (3.00%)** — Network congestion and transmission error indicator.
* **Avg SINR (12.01 dB)** — Average signal-to-interference-plus-noise ratio representing signal quality.
* **Avg RSRP (-94.89 dBm)** — Overall average reference signal received power representing signal strength.
* **Total Revenue Loss (GH₵ 410.72M)** — Aggregate financial impact linked to degraded cell site traffic and outages.

---

## 📊 Dashboard Visualizations & Business Questions Answered

### 1. Geographic Performance & Regional Equity
* **Visuals Used:** Regional Drop Call Rate Bar Chart & Region Filter.
* **Business Question Answered:** *Which regions in Ghana are experiencing the worst service degradation, and where are customers suffering the highest call drop rates?*
* **Insight:** Exposes regional disparities, showing **Upper West** (2.35%), **Eastern** (2.32%), and **Volta** (2.31%) recording the highest drop rates, enabling network operations to prioritize capital allocation.

### 2. Network Stability & Traffic Load Correlation
* **Visuals Used:** Longitudinal Trend Line Chart (*Drop Call Rate vs. Traffic Erlangs*).
* **Business Question Answered:** *Do traffic volume shifts over time correlate with network congestion and dropped calls across operational cycles?*
* **Insight:** Tracks monthly fluctuations comparing Drop Call Rates (hovering between 2.2% and 2.3%) against traffic volume (oscillating between 94K and 97K Erlangs) throughout 2025.

### 3. Equipment & Infrastructure Health
* **Visuals Used:** Site Health Donut Chart & Top 10 Packet Loss Bar Chart.
* **Business Question Answered:** *What percentage of our nationwide cell sites are at risk, and which specific towers are failing packet loss SLAs?*
* **Insight:** Reveals that **74.91%** (37.45K) of sites are optimal, while **17.97%** are in warning and **7.12%** are critical. The top-10 chart isolates rogue infrastructure (e.g., sites exceeding 3.7% packet loss) requiring immediate maintenance.

### 4. RF Interference and Commercial Risk (Subscriber Churn)
* **Visuals Used:** Scatter Plot (*SINR vs. Churn Risk*) & Stacked Area Chart (*Throughput by Technology*).
* **Business Question Answered:** *How does poor radio frequency (RF) signal quality directly drive customer dissatisfaction and financial churn?*
* **Insight:** Proves a strong inverse correlation: as SINR drops into negative or low single-digit dB values, churn risk spikes up to 30%. It also shows throughput performance across **4G LTE** (~33K footprint, GH₵ 268M revenue loss), **UMTS/3G** (~10K footprint, GH₵ 82M loss), and **5G NR** (~7K footprint, GH₵ 60M loss).

---

## 🛠️ Tools & Techniques Used

* **Python (`pandas`, `numpy`)** — Pipeline generation of 50,000-row realistic telemetry datasets across all 16 regions of Ghana.
* **MySQL Server** — Relational storage and performance-optimized SQL views (`v_cellular_customer_impact`).
* **Power BI & DAX** — Advanced data modeling, custom measures, and interactive reporting utilizing a clean 3-tier layout with custom gold-accented styling.

---
## Screenshot
<img width="1600" height="739" alt="image" src="https://github.com/user-attachments/assets/8c660fb5-8a20-4c64-b42f-e06a2f8770b4" />

## 🚀 Key Insights & Outcomes

* **RF Threshold Identification:** Cell sites operating below an SINR threshold of 5 dB experience a sharp upward trajectory in subscriber churn risk, establishing a hard operational engineering threshold for field interventions.
* **Revenue Protection & Financial Quantification:** Translating technical degradation into monetary figures (**GH₵ 410.72M** total impact, heavily weighted in 4G LTE at GH₵ 268M) provides leadership with precise justification for targeted network modernization and capacity expansion spend.
* **Proactive Infrastructure Risk Mitigation:** Identifying that nearly **25.09%** of nationwide cell sites reside in either "Warning" or "Critical" health states enables network management to transition from reactive break-fix cycles to predictive maintenance.
* **Regional Optimization Framework:** Highlighting structural disparities in northern and eastern corridors (Upper West, Eastern, Volta) ensures capital expenditure (CapEx) targets underserved sectors to narrow regional quality gaps.
