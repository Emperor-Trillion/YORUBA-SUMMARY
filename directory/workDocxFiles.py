import os
from docx import Document
import spacy
from collections import defaultdict

# Define entity labels
LABELS = {"PERSON", "GPE", "ORG", "LOC", "NORP", "EVENT", "WORK_OF_ART", "LANGUAGE", "PRODUCT"}

# Load spaCy model (you may need a multilingual model for Yoruba)
#nlp = spacy.load("xx_ent_wiki_sm")  # Multilingual model
nlp = spacy.load("en_core_web_sm")

def extract_articles(docx_path):
    """Extract articles separated by two newlines from a .docx file."""
    doc = Document(docx_path)
    full_text = "\n".join(para.text for para in doc.paragraphs)
    articles = [article.strip() for article in full_text.split("\n\n") if article.strip()]
    return articles

def extract_entities(text):
    """Extract entities from text and group them by label."""
    doc = nlp(text)
    entities = defaultdict(set)
    for ent in doc.ents:
        if ent.label_ in LABELS:
            entities[ent.label_].add(ent.text)
    return entities

def format_gazette(entities_by_label):
    """Format entities into gazette-style string."""
    output = ""
    for label in LABELS:
        words = entities_by_label.get(label, set())
        output += f"{label}{{\n"
        for word in sorted(words):
            output += f'    "{word}" : "",\n'
        output += "}\n\n"
    return output

def process_folder(folder_path, output_path):
    """Process all .docx files in the folder and generate gazette file."""
    combined_entities = defaultdict(set)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".docx"):
            docx_path = os.path.join(folder_path, filename)
            articles = extract_articles(docx_path)
            for article in articles:
                entities = extract_entities(article)
                for label, words in entities.items():
                    combined_entities[label].update(words)

    gazette_text = format_gazette(combined_entities)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(gazette_text)
    print(f"Gazette file saved to: {output_path}")


folder_path = "./Yoruba_Translated"
output_file = "./2_gazette.txt"
process_folder(folder_path, output_file)
