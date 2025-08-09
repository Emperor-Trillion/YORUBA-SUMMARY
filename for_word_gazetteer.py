import spacy
import os
import json
from collections import Counter

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Folder with your 15 text files
ARTICLES_DIR = "./textFiles"  # change if needed

# Entity types for translation (proper nouns)
TRANSLATE_LABELS = {"PERSON", "GPE", "ORG", "LOC", "NORP", "EVENT", "WORK_OF_ART", "LANGUAGE", "PRODUCT"}

# Containers for entities
translate_entities = Counter()

def process_text(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in TRANSLATE_LABELS:
            translate_entities[ent.text] += 1

def main():
    # Read all txt files
    for filename in os.listdir(ARTICLES_DIR):
        if filename.endswith(".txt"):
            path = os.path.join(ARTICLES_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                # Assuming articles separated by double newlines
                articles = content.split("\n\n")
                for article in articles:
                    process_text(article.strip())

    # Prepare gazetteers with empty strings for manual mapping
    translate_gazetteer = {entity: "" for entity in translate_entities.keys()}

    # Save to JSON files
    with open("translate_gazetteer.json", "w", encoding="utf-8") as f:
        json.dump(translate_gazetteer, f, indent=2, ensure_ascii=False)

    print(f"Found {len(translate_gazetteer)} translate entities.")
    print("Draft gazetteers saved as translate_gazetteer.json")

if __name__ == "__main__":
    main()
