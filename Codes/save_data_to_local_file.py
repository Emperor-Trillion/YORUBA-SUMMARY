from datasets import load_dataset
import pandas as pd

# Load the dataset from local cache
dataset = load_dataset(
    "cnn_dailymail",
    "3.0.0",
    cache_dir="/home/emperor/.cache/huggingface/datasets"
)

# Access the train split
train_data = dataset["train"]

# Convert first 300 rows to a pandas DataFrame
df_subset = train_data.select(range(300)).to_pandas()

# Keep only 'article' and 'highlights' columns
df_subset = df_subset[["article", "highlights"]]

# Export to CSV in current working directory
df_subset.to_csv("cnn_dailymail_subset2.csv", index=False)

print("✅ Exported cnn_dailymail_subset.csv to current folder.")
