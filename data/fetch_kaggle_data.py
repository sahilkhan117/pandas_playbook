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