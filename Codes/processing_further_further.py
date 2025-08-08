import re

def split_and_check_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    processed_lines = []

    def process_line(line):
        while line:
            line = line.strip()
            # Match: starts with capital, comma, 'v.', optional words, optional semicolon
            pattern = r'^[A-Z][^,]*,\s*v\..*?(?:;)?'
            match = re.match(pattern, line)
            if match:
                matched_part = match.group()
                remaining = line[len(matched_part):].lstrip()

                # Look for '.', "'", or '"'
                split_match = re.search(r'[.\'"]', remaining)
                if split_match:
                    split_index = split_match.start() + 1
                    processed_lines.append(matched_part + ' ' + remaining[:split_index])
                    line = remaining[split_index:].lstrip()
                else:
                    processed_lines.append(matched_part + ' ' + remaining)
                    break
            else:
                processed_lines.append(line)
                break

    for line in lines:
        process_line(line)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in processed_lines:
            outfile.write(line + '\n')

# 🛠 Example usage
input_file = 'final_segmented_final_merged_output.txt'  # Replace with your actual file
output_file = '2_final_segmented_final_merged_output.txt'

split_and_check_lines(input_file, output_file)
print(f"Segmented lines saved to: {output_file}")
