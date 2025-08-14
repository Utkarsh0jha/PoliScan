# 📊 POLISCAN – Election Contributions Analytics  
💡 *Turning U.S. political donation data into insights, trends, and transparency.*

---

## 📌 Overview 

Poliscan is an end-to-end big data analytics platform that leverages the publicly available OpenFEC (Federal Election Commission) datasets to uncover insights from U.S. political donation patterns. Built using a scalable AWS-based data pipeline architecture, the system enables political analysts, regulatory agencies, journalists, and the public to monitor political financing activities and detect anomalies with ease.

Our platform supports transparent, data-driven decisions in the electoral landscape by visualizing financial trends, flagging suspicious activities, and simplifying access to campaign finance data.

## 🗂 Datasets Used  

📂 **Primary Sources:**  
- 🗃️ [Individual Contributions Dataset](https://www.fec.gov/campaign-finance-data/contributions-individuals-file-description/) — All donations made by individuals  
- 🗃️ [Committee Master](https://www.fec.gov/campaign-finance-data/committee-master-file-description/) — Committees receiving contributions  
- 🗃️ [Candidate Master](https://www.fec.gov/campaign-finance-data/candidate-master-file-description/) — Candidate details, elections, and party affiliation  

---


## 🎯 Project Objectives
- [x] **Clean & structure** raw OpenFEC datasets (~40 GB) for analysis  
- [x] Identify **key features** — donation amounts, donor demographics, transaction types  
- [x] Detect **unusual or suspicious donations** using rule-based validation checks  
- [x] Create **interactive dashboards** to visualize donation patterns and anomalies  


## 🏛 Architecture  
Our system follows a **Medallion Architecture** with **Bronze, Silver, and Gold layers**:

1. **Bronze Layer** – Stores raw OpenFEC data for reference  
2. **Silver Layer** – Data cleaning, standardization, and enrichment (AWS Glue + Amazon EMR)  
3. **Gold Layer** – Optimized, query-ready data for analytics (Amazon Athena + Power BI)  

Architecture Diagram :

<img width="808" height="779" alt="image" src="https://github.com/user-attachments/assets/d8d226fa-9d0e-4a8f-87d3-aed9d7f450dc" />



🧾 Dataset Description
Primary Source: OpenFEC Individual Contributions Dataset

### 📄 Dataset Schema Overview

| Column Name                 |   Description                                               |
|-----------------------------|-------------------------------------------------------------|
| `CMTE_ID`                   | Committee receiving the contribution                        |
| `NAME`                      | Contributor's full name                                     |
| `CITY`, `STATE`, `ZIP_CODE` | Geographic location of the donor                            |
| `EMPLOYER`, `OCCUPATION`    | Donor's employment details                                  |
| `TRANSACTION_DT`            | Date of donation                                            |
| `TRANSACTION_AMT`           | Amount donated                                              |
| `TRANSACTION_TP`            | Type of donation                                            |
| `ENTITY_TP`                 | Entity type (e.g., `IND` = Individual)                      |
| `OTHER_ID`                  | FEC ID of contributor if not an individual                  |
| `SUB_ID`                    | Unique transaction identifier                               |




📈 Key KPIs & Metrics

| KPI                               |   Description                                                    |
|-----------------------------------|-------------------------------------------------------------------|
| Total Contributions               | Sum of all donations over a specific period.                      |
| Average Donation Size             | Mean contribution amount.                                         |
| Donor Retention Rate              | Percentage of repeat donors.                                      |
| Contribution Frequency            | Average number of donations per donor.                            |
| Refund Rate                       | Percentage of donations refunded.                                 |
| Earmarked Contribution Ratio      | Proportion of donations earmarked for specific purposes.          |
| Regional Contribution Distribution| Analysis of donations by geographic location.                     |
| Donor Demographics                | Breakdown of donors by occupation, employer, and gender.          |


**Services Used:**  
- ☁️ **AWS Glue** – ETL & schema discovery  
- 📜 **AWS Glue Crawler** – Automated schema inference  
- ⚡ **Amazon EMR (Spark)** – Large-scale distributed data processing  
- 🗄 **Amazon Athena** – Serverless SQL querying on S3  
- 📊 **Power BI** – Interactive dashboard & visualization

  



Use Cases:

•	Political Analysts & Researchers: Understand electoral dynamics, identify campaign finance trends, and support academic studies. 

•	Campaign Managers & Fundraisers: Optimize fundraising, allocate resources effectively, and analyze competitor strategies. 

•	Regulatory Bodies (e.g., FEC): Enhance compliance monitoring, fraud detection, and inform policy formulation. 

•	Investigative Journalists: Uncover influence and expose financial irregularities. 

•	Public & Advocacy Groups: Promote transparency and advocate for campaign finance reform.


---

## ✨ Impact
> POLISCAN transforms complex, large-scale political donation data into **clear, actionable insights**.  
> It empowers citizens, analysts, and regulators to **track money in politics**, ensuring **fairness, transparency, and trust** in the electoral process.

## Dashboard

ABOUT FEC:

<img width="1514" height="743" alt="image" src="https://github.com/user-attachments/assets/34f14a45-9811-4c89-a3a6-85d460eee51a" />

FEC DASHBOARD:

<img width="1342" height="737" alt="image" src="https://github.com/user-attachments/assets/4805d20b-5c21-4209-b26f-c78bd7e501ef" />

DEM AND REP PARTY:

<img width="1376" height="743" alt="image" src="https://github.com/user-attachments/assets/2e513803-f888-4be4-b486-324e4094dfea" />







