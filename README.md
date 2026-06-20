# 📊 NLP & Text Mining Pipeline for Customer Feedback Analysis

## 📌 Project Overview
This repository contains an automated text-mining data pipeline designed to ingest, clean, and categorize unstructured customer feedback logs. Built using Python and Pandas, this engine replaces manual text review with a programmatic batch-processing workflow. 

It utilizes Regular Expressions (Regex) to extract behavioral keywords and instantly flags high-risk operational complaints (e.g., Security Breaches, Deceptive Fees) for immediate triage.

## 🛠️ Technical Stack
* **Language:** Python
* **Data Processing:** Pandas, Glob (Batch File Processing)
* **Text Analytics:** Regular Expressions (`re` module), String Manipulation
* **Architecture:** Rule-based classification engine

## 💻 Quick Start (How to Run Locally)
1. **Clone the repository** to your local machine.
2. **Install the required dependencies:**
    ```
    pip install pandas
    ```
3. **Execute the pipeline engine:**
    ```
    python text_pipeline.py
    ```
4. **View the categorized output** in the newly generated `structured_risk_report.csv` file.

## ⚙️ How the Pipeline Works
1. **Batch Ingestion:** The script automatically scans a designated local directory (`/raw_logs/`) and merges multiple raw CSV flat-files into a unified master DataFrame, simulating a Data Lake ingestion process.
2. **Text Standardization:** Cleans unstructured text inputs by normalizing casing and stripping hidden whitespace.
3. **Pattern Recognition:** Scans paragraphs against a predefined dictionary of risk-indicator keywords using Regex.
4. **Structured Output:** Categorizes unstructured paragraphs into targeted operational buckets and exports an audit-ready `structured_risk_report.csv` for downstream dashboarding.

## 🚀 Business Value
By relying on lightweight Regex and rule-based text classification rather than heavy Machine Learning models, this pipeline serves as a highly efficient, production-ready triage tool. It processes massive amounts of text rows in milliseconds with zero training data required, ensuring 100% auditable categorization logic.