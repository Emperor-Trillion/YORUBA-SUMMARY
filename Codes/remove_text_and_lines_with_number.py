import re

def remove_digitized_lines(input_file, temp_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    cleaned_lines = []
    skip_next = False

    for line in lines:
        if skip_next:
            skip_next = False
            continue

        if "Digitized by Google" in line:
            skip_next = True  # Skip this line and the next one
            continue

        cleaned_lines.append(line)

    with open(temp_file, 'w') as out_file:
        out_file.writelines(cleaned_lines)


def remove_lines_with_numbers(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    final_lines = []
    for line in lines:
        if re.search(r'\d', line):  # Checks if any digit exists in the line
            continue
        final_lines.append(line)

    with open(output_file, 'w') as out_file:
        out_file.writelines(final_lines)


# 🛠 Example usage
original_file = 'merged_output.txt'
intermediate_file = 'temp_cleaned.txt'
final_output_file = 'fully_cleaned.txt'

remove_digitized_lines(original_file, intermediate_file)
remove_lines_with_numbers(intermediate_file, final_output_file)

print(f"Final cleaned file saved as: {final_output_file}")
