import re

def merge_non_alphanumeric_starts(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    merged_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:  # Skip empty lines
            continue

        # Check if line starts with non-alphanumeric character
        if not re.match(r'^[A-Za-z0-9]', stripped):
            if merged_lines:
                # Append to previous line with a space
                merged_lines[-1] = merged_lines[-1].rstrip('\n') + ' ' + stripped + '\n'
            else:
                # If it's the first line, just add it
                merged_lines.append(stripped + '\n')
        else:
            merged_lines.append(line)

    with open(output_file, 'w') as out_file:
        out_file.writelines(merged_lines)

# 🛠 Example usage
input_file = 'fully_cleaned.txt'  # Or any file you want to process
output_file = 'final_merged.txt'

merge_non_alphanumeric_starts(input_file, output_file)

print(f"Merged lines saved to: {output_file}")
