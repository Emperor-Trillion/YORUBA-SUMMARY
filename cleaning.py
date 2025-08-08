import re

def transform_line(line):
    # Regex to match lines like: Word, adj. definition.
    match = re.match(r'^(\w+),\s*(adj|n|v|adv|t|prep|i|aux|interj|pl|pron|pref|sing)\.\s*(.+)$', line.strip())
    if match:
        word, pos, definition = match.groups()
        # Capitalize part of speech
        pos_map = {
            'adj': 'Adjective',
            'n': 'Noun',
            'v': 'Verb',
            'adv': 'Adverb',
            't' : 'Transitive',
            'prep' : 'Preposition',
            'i' : 'Intransitive',
            'aux' : 'Auxiliary',
            'interj' : 'Interjection',
            'pl' : 'Plural',
            'pron' : 'Pronoun',
            'pref' : 'Prefix',
            'sing' : 'Singular'
        }
        pos_full = pos_map.get(pos.lower(), pos.capitalize())
        return f"{word}\t{pos_full}\t{definition}"
    return line.strip()

def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            transformed = transform_line(line)
            outfile.write(transformed + '\n')

# Example usage
input_file = 'yoruba_cleaned_output.txt'
output_file = '2_yoruba_cleaned_output.txt'
process_file(input_file, output_file)
