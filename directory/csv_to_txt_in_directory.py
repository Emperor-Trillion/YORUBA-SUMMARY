import pandas as pd
import os

# Define the source directory
source_dir = "/home/emperor/Yoruba-Summary/directory"

# List all CSV files in the source directory
csv_files = [f for f in os.listdir(source_dir) if f.endswith(".csv") and os.path.isfile(os.path.join(source_dir, f))]

# Process each CSV file
for csv_file in csv_files:
    csv_path = os.path.join(source_dir, csv_file)
    txt_filename = os.path.splitext(csv_file)[0] + ".txt"
    txt_path = os.path.join(source_dir, txt_filename)

    try:
        # Read the CSV file
        df = pd.read_csv(csv_path)

        # Ensure there are at least two columns
        if df.shape[1] < 2:
            print(f"⚠️ Skipping {csv_file}: less than two columns.")
            continue

        # Write to text file
        with open(txt_path, "w", encoding="utf-8") as f:
            for _, row in df.iterrows():
                first = str(row[0]).strip()
                second = str(row[1]).strip()
                f.write(first + "\n\n" + second + "\n\n")

        print(f"✅ Saved: {txt_path}")

    except Exception as e:
        print(f"❌ Error processing {csv_file}: {e}")
