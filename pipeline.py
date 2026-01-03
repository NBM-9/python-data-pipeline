import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['total_price'] = df['quantity'] * df['price']
    return df

def generate_summary(df):
    summary = df.groupby('region')['total_price'].sum().reset_index()
    return summary

def main():
    df = load_data('data/sales.csv')
    df = clean_data(df)
    summary = generate_summary(df)
    print(summary)

if __name__ == "__main__":
    main()
