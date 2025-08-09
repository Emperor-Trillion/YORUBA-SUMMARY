import os
import spacy
from collections import defaultdict

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define entity labels to extract
LABELS = {"PERSON", "GPE", "ORG", "LOC", "NORP", "EVENT", "WORK_OF_ART", "LANGUAGE", "PRODUCT"}

def extract_entities_from_folder(folder_path):
    entities_by_label = {label: defaultdict(str) for label in LABELS}

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                articles = content.split("\n\n")  # Split by two newlines

                for article in articles:
                    doc = nlp(article)
                    for ent in doc.ents:
                        if ent.label_ in LABELS:
                            entities_by_label[ent.label_][ent.text] = ""

    return entities_by_label

def write_gazette_file(entities_by_label, output_path):
    with open(output_path, "w", encoding="utf-8") as out_file:
        for label, entities in entities_by_label.items():
            out_file.write(f"{label}{{\n")
            for entity in sorted(entities):
                out_file.write(f'    "{entity}" : "",\n')
            out_file.write("}\n\n")

# 🔧 Set your folder and output file path
folder_path = "./textFiles"
output_file = "gazette.txt"

# 🚀 Run the extraction and write the gazette
entities = extract_entities_from_folder(folder_path)
write_gazette_file(entities, output_file)

print(f"Gazette file created at: {output_file}")
