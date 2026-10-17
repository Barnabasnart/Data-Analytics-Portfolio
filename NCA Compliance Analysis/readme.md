# 📡 NCA Quality of Service (QoS) Compliance Analysis

## 📌 Executive Summary
The **National Communications Authority (NCA)** regulates mobile telecommunication services across Ghana to safeguard consumer experience and enforce Quality of Service (QoS) standards. With strict regulatory updates mandating lower allowable **Call Drop Rates (CDR < 1%)**, higher **Call Connection Success Rates (CCSR > 95%)**, and data throughput thresholds across all Metropolitan, Municipal, and District Assemblies (MMDAs), non-compliance poses a catastrophic financial and operational risk to Mobile Network Operators (MNOs).

This project presents an enterprise-grade analytics solution evaluating **50,000 regulatory telemetry logs** across all 16 regions in Ghana. By translating raw technical KPIs into financial liability, the dashboard isolates high-risk cell sites, quantifies statutory penalty exposure (**GH₵ 2.0 Billion total risk**), and provides actionable network optimization pathways to eliminate regulatory breaches.

---

## 🎯 Key Performance Indicators (KPI Overview)

| Metric | Dashboard Value | Regulatory Standard / Context |
| :--- | :--- | :--- |
| **Overall Compliance Rate** | **5.02%** | Sites meeting all simultaneous NCA voice, data, and latency criteria. |
| **Non-Compliant Breaches** | **47,000** | Total recorded SLA violations across all network nodes. |
| **Average CCSR** | **97.01%** | National average Call Connection Success Rate (Target: > 95%). |
| **Average Call Drop Rate** | **2.50%** | National average Call Drop Rate (Target: < 1.00%). |
| **Average Data Throughput** | **80.17 Mbps** | Combined nationwide average download speed across 3G, 4G, and 5G. |
| **Total Audit Logs** | **50,000** | Monitored network telemetry records evaluated. |
| **Total Penalty Exposure** | **GH₵ 2.0 Billion** | Cumulative calculated statutory fine exposure under NCA penalty frameworks. |

---

## 📊 Business Questions Answered by Dashboard Visuals

### 1. Financial Risk Exposure: Total NCA Penalty (GHS) by Region
* **Chart Type:** Horizontal Clustered Bar Chart
* **Key Business Question Answered:** *Which regions in Ghana present the highest direct financial liability due to regulatory SLA breaches?*
* **Business Insight:** **Volta (GH₵ 143M)** and **Bono (GH₵ 140M)** lead nationwide penalty exposure, followed closely by Greater Accra (GH₵ 139M) and Northern (GH₵ 138M). Field engineering teams must prioritize CapEx and tower maintenance in these high-risk regional corridors first.

### 2. Nationwide Regulatory Compliance Audit: Compliant vs. Non-Compliant Nodes
* **Chart Type:** Donut Chart
* **Key Business Question Answered:** *What is the structural breakdown of network health across all evaluated nodes?*
* **Business Insight:** Only **10.41% (5.21K records)** fully pass all stringent regulatory criteria, while **89.59% (44.8K records)** trigger at least one SLA breach (primarily driven by the revised 1% Call Drop Rate cap).

### 3. Regulatory Breach Analysis: Failure Count by Network Technology
* **Chart Type:** Clustered Column Chart
* **Key Business Question Answered:** *Which network technology generation (3G, 4G, or 5G) accounts for the largest volume of compliance breaches?*
* **Business Insight:** **4G LTE** accounts for the vast majority of non-compliant breaches (**22K failures** vs. 3K compliant), followed by **UMTS 3G (13K failures)** and **5G NR (9K failures)**. This highlights that 4G backhaul congestion and RF interference are the primary root causes of network-wide non-compliance.

### 4. Voice Quality Audit: Call Connection Success Rate (%) vs. Drop Call Rate (%)
* **Chart Type:** Scatter Plot with Compliance Quadrants
* **Key Business Question Answered:** *How do voice setup reliability and call retention correlate across individual cell sites?*
* **Business Insight:** Isolates compliant cell sites in the bottom-right quadrant ($CCSR > 95\%$ AND $Drop Call Rate < 1\%$). Sites falling into the upper-left cluster ($CSSR < 95\%$ or $Drop Call Rate \ge 1\%$) are flagged as critical non-compliant nodes requiring immediate antenna tilting and power adjustments.

### 5. Top 10 Cell Sites With High Penalty Exposure
* **Chart Type:** Horizontal Bar Chart
* **Key Business Question Answered:** *Which specific base stations generate the highest localized financial risk?*
* **Business Insight:** Base station **`GHA_SITE_1493`** is the single largest financial liability, generating **GH₵ 1.97M** in potential fines, followed by `GHA_SITE_1491` (**GH₵ 1.75M**) and `GHA_SITE_1498` (**GH₵ 1.70M**). Dispatching field technicians to just these top 10 sites resolves over **GH₵ 14 Million** in penalty exposure.

### 6. Regulatory Risk Trajectory: Cumulative Monthly NCA Penalty Exposure (GHS)
* **Chart Type:** Line Trend Chart
* **Key Business Question Answered:** *How does financial risk exposure fluctuate throughout the operational year?*
* **Business Insight:** Penalty risk peaks in **July (GH₵ 190.0M)** and **January (GH₵ 188.9M)** due to seasonal traffic congestion and rainy season signal degradation, dipping to its lowest point in **February (GH₵ 167.7M)**.

### 7. Data Performance Audit: Average Throughput vs. Packet Loss by Region
* **Chart Type:** Combo Chart (Bar + Line)
* **Key Business Question Answered:** *Are data throughput bottlenecks driven by high packet loss across regional nodes?*
* **Business Insight:** While data throughput remains relatively uniform (~79–81 Mbps), packet loss fluctuates significantly—peaking in **Ashanti (2.61%)** and **Northern (2.58%)**.

---
## Screenshot
<img src="NCA Compliance Analysis.jpg" alt="NCA Compliance Analysis Dashboard" width="100%" />

## 🛠️ Technical Stack & Architecture

* **Data Processing & Feature Engineering:** Python (`pandas`, `numpy`) for synthetic telemetry generation and threshold labeling.
* **Business Intelligence:** Power BI (Complex DAX measures, dynamic parameters, custom dark-mode UI layout).

---

