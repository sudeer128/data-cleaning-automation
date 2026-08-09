import pandas as pd

def clean_data(file_path, output_path):
    df = pd.read_csv(file_path)
    df = df.drop_duplicates()
    df = df.fillna(method='ffill')
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.to_csv(output_path, index=False)
    print("Cleaned data saved to", output_path)

# Example usage:
# clean_data("raw_data.csv", "cleaned_data.csv")
