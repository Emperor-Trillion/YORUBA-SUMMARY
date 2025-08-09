""""
This code scans a folder to replace defined in my gazetteer.json, in the exact same casing, and put output files in a specified directory.

load_gazetteer: Loads the JSON gazetteer, sorts keys longest first to avoid partial replacements (e.g. replacing "Nixon" before "Richard Nixon").

replace_text: Replaces all occurrences of each gazetteer key with its some sort of Yoruba equivalent in the text which may not be exactly accurate replacement in context.

localize_text_files: Reads each .txt file from input folder, runs replacements, saves to output folder.
"""

import os
import json
import re

def load_gazetteer(gazetteer_path):
    with open(gazetteer_path, 'r', encoding='utf-8') as f:
        gazetteer = json.load(f)
    # Sort keys by length descending to replace longer matches first (avoid partial overlaps)
    sorted_keys = sorted(gazetteer.keys(), key=len, reverse=True)
    return gazetteer, sorted_keys

def replace_text(text, gazetteer, sorted_keys):
    # Escape keys for regex and use word boundaries for exact matching if needed
    # But since some keys are multiword or proper nouns, we avoid \b for phrases.
    for key in sorted_keys:
        # Use re.escape for safe regex matching
        pattern = re.escape(key)
        text = re.sub(pattern, gazetteer[key], text)
    return text

def localize_text_files(input_folder, output_folder, gazetteer_path):
    # Load gazetteer
    gazetteer, sorted_keys = load_gazetteer(gazetteer_path)

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through files in input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.txt'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()

            localized_content = replace_text(content, gazetteer, sorted_keys)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(localized_content)

            print(f"Processed and saved: {filename}")

# Usage example
if __name__ == "__main__":
    input_dir = "./textFiles"
    output_dir = "./replacedTextFiles"
    gazetteer_json_path = "./entities_filled.json"

    localize_text_files(input_dir, output_dir, gazetteer_json_path)
