import pandas as pd

def run_etl():
    # Step 1: Load data from web
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
    df = pd.read_csv(url)

    # Step 2: Clean data
    df.dropna(inplace=True)  # Drop missing if any
    df['day'] = df['day'].str.capitalize()  # Capitalize day names

    # Step 3: Feature engineering - calculate tip percentage
    df['tip_pct'] = (df['tip'] / df['total_bill']) * 100

    # Step 4: Aggregate: average tip and total bill by day and time
    agg_df = df.groupby(['day', 'time']).agg(
        avg_tip_pct=('tip_pct', 'mean'),
        avg_total_bill=('total_bill', 'mean'),
        count=('tip', 'count')
    ).reset_index()

    # Step 5: Save processed data
    agg_df.to_csv('data/processed_tips_data.csv', index=False)
    print('ETL completed and processed_tips_data.csv saved.')

if __name__ == '__main__':
    run_etl()
