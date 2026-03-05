# Customer Sentiment Analysis Pipeline

## Project Overview
This project demonstrates a complete data workflow: importing raw customer data, merging it with feedback text, and using Python logic to categorize sentiment (Positive, Negative, or Neutral). 

## Key Features
- **Data Merging:** Uses Pandas to join disparate datasets on a shared key (`name`).
- **Automated Analysis:** Utilizes keyword-based sentiment classification.
- **Visual Reporting:** Generates bar charts using Matplotlib to show sentiment distribution by city.
- **Export Ready:** Outputs a clean, analyzed CSV file for business stakeholders.

## Technical Skills Used
- **Language:** Python 3.x
- **Libraries:** Pandas, Matplotlib, OS, IO
- **Concepts:** List Comprehensions, Function Mapping, Dataframe Merging

## How to Run
1. Ensure you have the input files (`Customer_Data.csv` and `customer_feedback.csv`) in the directory.
2. Run `customer_feedback.py`.
3. View the results in `analyzed_customer_feedback.csv` and the generated chart.
