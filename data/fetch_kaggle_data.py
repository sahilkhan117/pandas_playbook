# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "cancer-data.csv"

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "erdemtaha/cancer-data",
  file_path,
  pandas_kwargs={"encoding": "latin1"}
)

print("First 5 records:", df.head())
df.to_csv("data/raw/cancer-data.csv", index=False)

# i use 4 datasets from kaggle use them
# 1.  world gdp growth data from `sazidthe1/world-gdp-growth`
# 2.  amazon sales data from `zahidmughal2343/amazon-sales-2025`
# 3.  cancer data from `erdemtaha/cancer-data`
# 4.  NIFTY-50 data from `rohanrao/nifty50-stock-market-data`
