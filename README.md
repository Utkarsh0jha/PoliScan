#POLYSCAN – Election Contributions Analytics

📌 Overview

Polyscan is an end-to-end big data analytics platform that leverages the publicly available OpenFEC (Federal Election Commission) datasets to uncover insights from U.S. political donation patterns. Built using a scalable AWS-based data pipeline architecture, the system enables political analysts, regulatory agencies, journalists, and the public to monitor political financing activities and detect anomalies with ease.

Our platform supports transparent, data-driven decisions in the electoral landscape by visualizing financial trends, flagging suspicious activities, and simplifying access to campaign finance data.


Main dataset:

https://www.fec.gov/campaign-finance-data/contributions-individuals-file-description/

https://www.fec.gov/campaign-finance-data/committee-master-file-description/

https://www.fec.gov/campaign-finance-data/candidate-master-file-description/


Individuals → Committees: Contributions are made to committees (CMTE_ID).

Committees → Candidates: Committees are linked to candidates (CAND_ID or CAND_PCC).

Candidates → Elections: Candidate data includes election year, office, and party.



🚀 The primary objectives of this project are:

To clean and structure the OpenFEC individual contributions dataset to ensure it is suitable for analysis.

To identify and organize key features—such as donation amounts, donor demographics, and transaction types—that influence donation patterns.

To detect unusual or potentially suspicious donations through well-defined, rule-based validation checks (excluding the use of machine learning).

To derive meaningful insights into donor behavior, including geographic origin, employment details, and socio-economic background.

To present complex trends and anomalies in political donations through clear, intuitive visualizations.

To develop a robust system or dashboard that enables analysts, campaign teams, and regulatory authorities to effectively explore and interpret political contribution data.


System Architecture



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



Expected Outcomes:

•	A deployable dashboard for public or organizational use.

•	A clean and well-organized dataset ready for analysis.

•	Clear understanding of what factors influence political donations.

•	Detection of unusual or suspicious donation activities.

•	Insights into who is donating — based on location, job, and gender.

•	Easy-to-read charts and visuals showing donation trends and red flags.

•	A useful tool or system that helps others (like analysts or officials) explore and understand political donation data.



Use Cases:

•	Political Analysts & Researchers: Understand electoral dynamics, identify campaign finance trends, and support academic studies. 

•	Campaign Managers & Fundraisers: Optimize fundraising, allocate resources effectively, and analyze competitor strategies. 

•	Regulatory Bodies (e.g., FEC): Enhance compliance monitoring, fraud detection, and inform policy formulation. 

•	Investigative Journalists: Uncover influence and expose financial irregularities. 

•	Public & Advocacy Groups: Promote transparency and advocate for campaign finance reform.



This project helps turn complex political donation data into clear and useful information. It allows people like analysts, campaign teams, and officials to see patterns, find unusual donations, and better understand who is funding politics.
By making this information easier to explore, the project supports fairness, transparency, and trust in the election process. It gives the tools needed to keep political financing open and accountable — helping strengthen democracy in the U.S.





