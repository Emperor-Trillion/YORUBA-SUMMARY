def merge_lines(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    merged_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue  # skip empty lines

        if merged_lines:
            first_char = stripped[0]
            if first_char.islower() and not first_char.isdigit():
                # Merge with previous line
                merged_lines[-1] += ' ' + stripped
                continue

        merged_lines.append(stripped)

    # Write the result to a new file
    with open(output_file, 'w') as out_file:
        for line in merged_lines:
            out_file.write(line + '\n')


# Example usage
input_path = 'yoruba_dictionary_words.txt'
output_path = 'merged_output.txt'
merge_lines(input_path, output_path)
print(f"Processed text saved to {output_path}")
