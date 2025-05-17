
# 📊 SalesDashboard

This project is a complete end-to-end data analytics solution that demonstrates how to build a sales (tips) dashboard using **Python**, **Power BI**, and **Streamlit**. It covers everything from ETL to static and interactive data visualizations, making it a great showcase for data engineering and analytics skills.

---

## 🧱 Project Structure

SalesDashboard/
├── data/ 
│ ├── raw_tips_data.csv
│ └── processed_tips_data.csv
├── etl/ 
│ └── etl_process.py
├── analysis/ 
│ └── sales_analysis.py
├── visuals/ 
│ ├── avg_tip_pct_by_day_time.png
│ ├── total_bill_distribution.png
│ ├── tip_pct_vs_total_bill.png
│ └── tips_by_day_count.png
├── dashboard/ 
│ └── TipsDashboard.pbix
├── interactive_dashboard/ 
│ └── streamlit_app.py
├── requirements.txt 
└── README.md 

---

## 🔁 ETL Pipeline

The ETL script performs the following:
- Loads `tips.csv` from a public URL
- Cleans and transforms the data
- Calculates tip percentages
- Saves the result to `data/processed_tips_data.csv`

📄 File: `etl/etl_process.py`

### Run ETL:
```bash
python etl/etl_process.py
📈 Static Visualizations
Visuals are created using matplotlib and seaborn and saved in /visuals:

Average Tip % by Day and Time

Total Bill Distribution

Tip % vs Total Bill

Number of Tips by Day

📄 File: analysis/sales_analysis.py

Run Analysis:
bash
Copy
Edit
python analysis/sales_analysis.py
🧠 Power BI Dashboard
A visually interactive .pbix report built on the processed CSV data.

📄 File: dashboard/TipsDashboard.pbix

Includes:

Bar charts for tip trends

Filters by day/time/gender

Comparative visuals for total bill vs tip

Open with Power BI Desktop.

🌐 Streamlit Interactive App
A web-based interactive dashboard where users can explore:

Tip % by day

Tip % vs total bill (scatter)

Table of filtered records

📄 File: interactive_dashboard/streamlit_app.py

Run Dashboard:
bash
Copy
Edit
streamlit run interactive_dashboard/streamlit_app.py
💾 Requirements
Install Python dependencies:

bash
Copy
Edit
pip install -r requirements.txt
requirements.txt
nginx
Copy
Edit
pandas
matplotlib
seaborn
streamlit
📊 Dataset Info
Dataset: tips.csv from Seaborn’s demo datasets



