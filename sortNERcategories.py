import json
import spacy
from collections import defaultdict

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Define the entity labels to sort by
LABELS = {"PERSON", "GPE", "ORG", "LOC", "NORP", "EVENT", "WORK_OF_ART", "LANGUAGE", "PRODUCT"}

# Load the gazetteer JSON file
with open("translate_gazetteer.json", "r", encoding="utf-8") as f:
    gazetteer = json.load(f)

# Create a dictionary to group entries by entity label
grouped = defaultdict(dict)

for key in gazetteer.keys():
    doc = nlp(key)
    for ent in doc.ents:
        if ent.label_ in LABELS:
            grouped[ent.label_][key] = ""
            break  # Only assign to the first matching label

# Save to a custom-formatted text file
with open("grouped_entities.txt", "w", encoding="utf-8") as f:
    for label in LABELS:
        if label in grouped:
            f.write(f"{label}{{\n")
            for key in grouped[label]:
                f.write(f'  "{key}" : "",\n')
            f.write("}\n\n")

print("✅ Grouped entities saved to 'grouped_entities.txt'")
