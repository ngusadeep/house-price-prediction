import os
import tarfile
from six.moves import urllib
import pandas as pd

#download data
HOUSING_URL = "https://github.com/ageron/data/raw/main/housing.tgz"
HOUSING_PATH = os.path.join("datasets", "housing")

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    alt_csv_path = os.path.join(housing_path, "housing", "housing.csv")
    if os.path.exists(csv_path) or os.path.exists(alt_csv_path):
        print("Data already downloaded and extracted.")
        return
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    with tarfile.open(tgz_path) as housing_tgz:
        housing_tgz.extractall(path=housing_path)
    print("Download and extraction complete.")

# Now when you call fetch_housing_data(), it creates a datasets/housing directory in your workspace, downloads the housing.tgz file, and extracts the housing.csv from it in this directory. Now let’s load the data using Pandas. Once again you should write a small function to load the data:
# Load dataset into pandas DataFrame
def load_housing_data(housing_path=HOUSING_PATH):
    # Try the default location
    csv_path = os.path.join(housing_path, "housing.csv")
    if os.path.exists(csv_path):
        return pd.read_csv(csv_path)
    # Try inside a subfolder (sometimes the tarball extracts to housing/housing/housing.csv)
    alt_csv_path = os.path.join(housing_path, "housing", "housing.csv")
    if os.path.exists(alt_csv_path):
        return pd.read_csv(alt_csv_path)
    # If not found, raise a clear error
    raise FileNotFoundError(f"housing.csv not found in {csv_path} or {alt_csv_path}")
