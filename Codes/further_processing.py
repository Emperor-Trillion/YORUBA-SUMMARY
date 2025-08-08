def clean_lines_from_file(input_path, output_path):
    # Read lines from input file
    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    cleaned = []
    skip_next = False

    for i in range(len(lines) - 1):
        if skip_next:
            skip_next = False
            continue

        current = lines[i].strip()
        next_line = lines[i + 1].strip()

        # If current line ends in comma or space
        if current.endswith(',') or current.endswith(' '):
            # If next line also ends in comma or space → delete both
            if next_line.endswith(',') or next_line.endswith(' '):
                skip_next = True
                continue
            else:
                # Merge lines
                merged = current + ' ' + next_line
                cleaned.append(merged)
                skip_next = True
        else:
            cleaned.append(current)

    # Handle last line if it wasn't part of a pair
    if not skip_next and len(lines) > 0:
        cleaned.append(lines[-1].strip())

    # Write cleaned lines to output file
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for line in cleaned:
            outfile.write(line + '\n')

# Example usage
input_file = 'final_merged.txt'
output_file = 'final_merged_output.txt'
clean_lines_from_file(input_file, output_file)
