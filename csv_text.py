import csv
import os

def extract_column_and_write_chunks(csv_path, output_dir, column_index=0, chunk_size=20):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read the CSV and extract the specified column
    with open(csv_path, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        entries = [row[column_index].strip() for row in reader if len(row) > column_index]

    # Write entries to multiple text files
    for i in range(0, len(entries), chunk_size):
        chunk = entries[i:i + chunk_size]
        output_path = os.path.join(output_dir, f'output_chunk_{i // chunk_size + 1}.txt')
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write('\n\n'.join(chunk))

    print(f"✅ Done! Created {((len(entries) - 1) // chunk_size) + 1} files in '{output_dir}'.")

# Example usage
csv_file = 'cnn_dailymail_subset.csv'
output_folder = './textFiles'
extract_column_and_write_chunks(csv_file, output_folder)
