import pandas as pd

# Load the CSV file
df = pd.read_csv("cnn_dailymail_subset.csv")

# Select rows 1 to 300 (excluding row 0)
subset = df.iloc[1:301]

# Split into 10 chunks of 30 rows each
chunk_size = 30
for i in range(10):
    start = i * chunk_size 
    end = start + chunk_size
    chunk = subset.iloc[start:end]
    
    # Save each chunk to a separate CSV file
    filename = f"cnn_dailymail_part_{i+1}.csv"
    chunk.to_csv(filename, index=False)
    print(f"✅ Saved {filename} with rows {start+1} to {end}")
