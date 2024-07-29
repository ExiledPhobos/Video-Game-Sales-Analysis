Video Game Sales Analysis

- Project Description
This project provides a comprehensive analysis of video game sales data. The analysis includes data cleaning, exploratory data analysis (EDA), and visualizations to uncover trends and insights. The dataset contains information on video game sales across various platforms, genres, and regions.

- Project Structure

video-game-sales-analysis/
├── data/
│   ├── raw/
│   │   └── vgsales.csv
│   └── processed/
│       └── vgsales_cleaned.csv
├── scripts/
│   ├── data_cleaning.py
│   ├── eda_and_visualization.py
├── reports/
│   ├── figures/
│   │   ├── distribution_year.png
│   │   ├── distribution_genres.png
│   │   ├── distribution_platforms.png
│   │   ├── top_publishers.png
│   │   ├── correlation_matrix.png
│   │   ├── sales_by_year.png
│   │   ├── top_genres.png
│   │   ├── top_platforms.png
│   │   ├── top_publishers.png
│   │   └── sales_by_region.png
│   └── summary_report.md
├── .gitignore
├── README.md
└── requirements.txt

- Setup Instructions

1. Clone the repository: git clone https://github.com/your-username/video-game-sales-analysis.git

2. Navigate to the project directory: cd video-game-sales-analysis

3. Set up a virtual environment:

   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. Install the dependencies: pip install -r requirements.txt

- Usage

1. Run `scripts/data_cleaning.py` to clean the raw data.

2. Run `scripts/eda_and_visualization.py` to perform EDA and generate visualizations.

- Results

The results of the analysis can be found in the `reports/figures` directory, and the summary of the findings is documented in `reports/summary_report.md`.