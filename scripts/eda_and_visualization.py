import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the path to the processed data
processed_data_path = 'C:/Users/exile/Documents/GitHub/video-game-sales-analysis/data/processed/vgsales_cleaned.csv'
figures_path = 'C:/Users/exile/Documents/GitHub/video-game-sales-analysis/reports/figures/'

# Load the cleaned data
def load_data(path):
    return pd.read_csv(path)

# Perform Exploratory Data Analysis
def perform_eda(df):
    # Display basic information about the dataset
    print("Basic Information:")
    print(df.info())

    # Display basic statistics
    print("\nBasic Statistics:")
    print(df.describe())

    # Display the first few rows of the dataset
    print("\nFirst few rows:")
    print(df.head())

def plot_visualizations(df):
    # Plot the distribution of numerical features
    plt.figure(figsize=(10, 6))
    df['Year'].hist(bins=30, edgecolor='black', color='#86bf91')
    plt.title('Distribution of Year')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.grid(False)
    plt.savefig(f'{figures_path}distribution_year.png')
    plt.show()

    # Plot the distribution of categorical features
    plt.figure(figsize=(10, 6))
    sns.countplot(y='Genre', data=df, order=df['Genre'].value_counts().index, hue='Genre', palette='Set2', dodge=False)
    plt.title('Distribution of Genres')
    plt.xlabel('Count')
    plt.ylabel('Genre')
    plt.legend([], [], frameon=False)
    plt.savefig(f'{figures_path}distribution_genres.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.countplot(y='Platform', data=df, order=df['Platform'].value_counts().index, hue='Platform', palette='Set3', dodge=False)
    plt.title('Distribution of Platforms')
    plt.xlabel('Count')
    plt.ylabel('Platform')
    plt.legend([], [], frameon=False)
    plt.savefig(f'{figures_path}distribution_platforms.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.countplot(y='Publisher', data=df, order=df['Publisher'].value_counts().index[:10], hue='Publisher', palette='Paired', dodge=False)
    plt.title('Top 10 Publishers')
    plt.xlabel('Count')
    plt.ylabel('Publisher')
    plt.legend([], [], frameon=False)
    plt.savefig(f'{figures_path}top_publishers.png')
    plt.show()

    # Plot the correlation matrix for numerical columns only
    plt.figure(figsize=(10, 6))
    numerical_df = df.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.savefig(f'{figures_path}correlation_matrix.png')
    plt.show()

    # Plot sales distribution by year
    plt.figure(figsize=(12, 6))
    yearly_sales = df.groupby('Year')['Global_Sales'].sum().reset_index()
    sns.lineplot(x='Year', y='Global_Sales', data=yearly_sales, marker='o', color='b')
    plt.title('Global Sales Distribution by Year')
    plt.xlabel('Year')
    plt.ylabel('Global Sales (in millions)')
    plt.grid(True)
    plt.savefig(f'{figures_path}sales_by_year.png')
    plt.show()

    # Plot top genres by global sales
    plt.figure(figsize=(12, 6))
    top_genres = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).head(10).reset_index()
    sns.barplot(x='Global_Sales', y='Genre', data=top_genres, hue='Genre', palette='Set2', dodge=False)
    plt.title('Top 10 Genres by Global Sales')
    plt.xlabel('Global Sales (in millions)')
    plt.ylabel('Genre')
    plt.legend([], [], frameon=False)
    plt.savefig(f'{figures_path}top_genres.png')
    plt.show()

    # Plot top platforms by global sales
    plt.figure(figsize=(12, 6))
    top_platforms = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10).reset_index()
    sns.barplot(x='Global_Sales', y='Platform', data=top_platforms, hue='Platform', palette='Set3', dodge=False)
    plt.title('Top 10 Platforms by Global Sales')
    plt.xlabel('Global Sales (in millions)')
    plt.ylabel('Platform')
    plt.legend([], [], frameon=False)
    plt.savefig(f'{figures_path}top_platforms.png')
    plt.show()

    # Plot top publishers by global sales
    plt.figure(figsize=(12, 6))
    top_publishers = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10).reset_index()
    sns.barplot(x='Global_Sales', y='Publisher', data=top_publishers, hue='Publisher', palette='Paired', dodge=False)
    plt.title('Top 10 Publishers by Global Sales')
    plt.xlabel('Global Sales (in millions)')
    plt.ylabel('Publisher')
    plt.legend([], [], frameon=False)
    plt.savefig(f'{figures_path}top_publishers.png')
    plt.show()

    # Plot sales distribution by region
    plt.figure(figsize=(12, 6))
    regional_sales = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum().reset_index()
    regional_sales.columns = ['Region', 'Sales']
    sns.barplot(x='Sales', y='Region', data=regional_sales, hue='Region', palette='viridis', dodge=False)
    plt.title('Sales Distribution by Region')
    plt.xlabel('Sales (in millions)')
    plt.ylabel('Region')
    plt.legend([], [], frameon=False)
    plt.savefig(f'{figures_path}sales_by_region.png')
    plt.show()

def main():
    # Load data
    df = load_data(processed_data_path)

    # Perform EDA
    perform_eda(df)

    # Plot visualizations
    plot_visualizations(df)

if __name__ == '__main__':
    main()