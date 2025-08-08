def merge_lowercase_or_hyphen_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    merged_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue  # Skip empty lines

        first_char = stripped[0]
        if merged_lines and (first_char.islower() or first_char == '-'):
            # Merge with previous line
            merged_lines[-1] = merged_lines[-1].rstrip('\n') + ' ' + stripped + '\n'
        else:
            merged_lines.append(stripped + '\n')

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(merged_lines)

# 🛠 Example usage
input_file = '2_final_segmented_final_merged_output.txt'  # Or any file you want to process
output_file = '3_final_segmented_final_merged_output.txt'

merge_lowercase_or_hyphen_lines(input_file, output_file)
print(f"Merged lowercase/hyphen lines saved to: {output_file}")
