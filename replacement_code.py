"""
This code 

Read your JSON file containing extracted entities (currently with empty values).

Detect each entity’s category automatically using SpaCy NER.

Assign Yoruba replacements from a predefined replacement bank for that category.

Cycle through the Yoruba list so it uses most of the list before repeating, 

to avoid repetitive replacements."""


import json
import random
import spacy
from collections import defaultdict

# Load English SpaCy model
nlp = spacy.load("en_core_web_sm")

# Load Yoruba replacement bank from JSON file
with open("yoruba_replacement_bank.json", "r", encoding="utf-8") as f:
    replacement_bank = json.load(f)

# Function to create cycling generator for replacements
def cycling_generator(items):
    while True:
        shuffled = items[:]
        random.shuffle(shuffled)
        for item in shuffled:
            yield item

# Create a generator for each category
replacement_generators = {cat: cycling_generator(words) for cat, words in replacement_bank.items()}

# Load your extracted entities JSON
with open("translate_gazetteer.json", "r", encoding="utf-8") as f:
    entities_dict = json.load(f)

# Function to detect entity category
def get_entity_label(text):
    doc = nlp(text)
    for ent in doc.ents:
        return ent.label_
    return None

# Fill replacements
for entity, current_value in entities_dict.items():
    category = get_entity_label(entity)
    if category in replacement_generators:
        entities_dict[entity] = next(replacement_generators[category])
    else:
        # If entity category not in bank, just keep it unchanged or add custom handling
        entities_dict[entity] = entity

# Save filled JSON
with open("entities_filled.json", "w", encoding="utf-8") as f:
    json.dump(entities_dict, f, ensure_ascii=False, indent=2)

print("✅ Yoruba replacements assigned successfully!")
