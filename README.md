## Customer Risk Scoring Using Transaction Behavior (Excel-Based Analytics)
## Executive Summary

This project demonstrates how simple transaction behavior indicators can be combined into a transparent risk scoring framework to support customer prioritization for compliance reviews. Using Excel and Python, I developed a weighted risk score based on transaction frequency, average transaction value, and jurisdiction exposure. The results show how a risk-based approach can help focus compliance resources on higher-risk customers while reducing unnecessary reviews.

## 1. Business Context

Financial institutions must balance regulatory obligations with operational efficiency. Traditional rule-based monitoring often generates excessive alerts, many of which represent low-risk customers. This creates review backlogs and strains compliance teams.

A risk-based prioritization model helps ensure that investigative effort is focused where it matters most.

## 2. Business Question

Which customers should be prioritized for compliance review based on observable transaction behavior and jurisdiction exposure?

## 3. Data Description

This analysis uses a simulated customer-level dataset designed to reflect realistic AML monitoring scenarios while avoiding confidentiality and privacy concerns.

## Key Variables

customer_id – Unique customer identifier

txn_count – Number of transactions over a 30-day period

avg_txn_amount – Average transaction value

high_risk_country – Indicator of exposure to higher-risk jurisdictions (1 = Yes, 0 = No)

flagged – Simulated indicator of whether the customer was reviewed

txn_norm – Normalized transaction frequency

amt_norm – Normalized transaction value

risk_score – Weighted risk score

Simulated data allows the focus to remain on analytical logic, explainability, and decision-making rather than proprietary information.

## 4. Methodology

Created a simulated dataset representing customer transaction behavior

Normalized transaction frequency and transaction value to a 0–1 scale

Designed a transparent, rule-based risk score using weighted indicators

Ranked customers based on overall risk score

Interpreted results to support compliance prioritization decisions

Risk Score Formula
Risk Score = (0.4 × Transaction Frequency) 
           + (0.4 × Transaction Amount) 
           + (0.2 × High-Risk Jurisdiction Indicator)


 ##Weights were selected to emphasize behavioral risk, while still accounting for jurisdiction exposure.

## 5. Key Findings

Customers with higher transaction frequency and larger average transaction values consistently received higher risk scores.

Exposure to high-risk jurisdictions increased risk, but behavioral indicators had a stronger influence on overall prioritization.

Several customers with jurisdiction exposure alone remained low-risk due to minimal transaction activity, supporting a balanced, risk-based approach.

## 6. Business Interpretation

The results demonstrate that not all customers linked to higher-risk jurisdictions require immediate review. Instead, combining behavioral indicators with jurisdiction exposure enables compliance teams to better differentiate between high-priority and low-priority cases, improving efficiency without compromising regulatory expectations.

## 7. Recommendations

Use a transparent, weighted risk scoring approach to prioritize customer reviews.

Focus investigative resources on customers with elevated behavioral risk rather than jurisdiction alone.

Regularly review and adjust weights as transaction patterns or regulatory guidance evolve.

## 8. Limitations & Next Steps

## Limitations

Data is simulated and simplified for demonstration purposes.

The model does not include transaction sequencing or network relationships.

## Next Steps

Introduce risk buckets (Low / Medium / High) to support operational workflows.

Replicate the logic in Python or SQL for scalability.

Compare rule-based scoring with basic statistical or machine learning models.

9. Repository Contents
📁 customer-risk-scoring-excel
 ├── customer_risk_scoring.xlsx
 ├── README.md

## Why This Project Matters

This project highlights the ability to:

Translate compliance needs into analytical logic

Build explainable, business-friendly models

Communicate insights clearly to non-technical stakeholders

[Customer Risk Scoring.xlsx](https://github.com/user-attachments/files/24259106/Customer.Risk.Scoring.xlsx)

