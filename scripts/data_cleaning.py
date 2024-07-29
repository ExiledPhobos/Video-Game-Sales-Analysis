import pandas as pd

# Define the path to the raw data
raw_data_path = 'C:/Users/exile/Documents/GitHub/video-game-sales-analysis/data/raw/vgsales.csv'

# Define the path to save the processed data
processed_data_path = 'C:/Users/exile/Documents/GitHub/video-game-sales-analysis/data/processed/vgsales_cleaned.csv'

# Load the raw data
def load_data(path):
    return pd.read_csv(path)

# Perform data cleaning
def clean_data(df):
    # Drop rows with missing values
    df = df.dropna()

    # Correct data types if necessary
    df.loc[:, 'Year'] = df['Year'].astype(int)

    # Correcting categorical data
    df.loc[:, 'Genre'] = df['Genre'].str.capitalize()
    df.loc[:, 'Platform'] = df['Platform'].str.upper()

    return df

# Save the cleaned data
def save_data(df, path):
    df.to_csv(path, index=False)

def main():
    # Load data
    df = load_data(raw_data_path)

    # Clean data
    df_cleaned = clean_data(df)

    # Save cleaned data
    save_data(df_cleaned, processed_data_path)

    print(f"Data cleaning complete. Cleaned data saved to {processed_data_path}")

if __name__ == '__main__':
    main()