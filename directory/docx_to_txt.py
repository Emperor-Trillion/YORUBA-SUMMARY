import os
from docx import Document

def docx_to_txt(docx_path, txt_path):
    """Extract text from a .docx file and save it to a .txt file."""
    doc = Document(docx_path)
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        for para in doc.paragraphs:
            txt_file.write(para.text + '\n')

def convert_all_docx_in_folder(folder_path):
    """Convert all .docx files in the folder to .txt files."""
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.docx'):
            docx_path = os.path.join(folder_path, filename)
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_path = os.path.join(folder_path, txt_filename)
            docx_to_txt(docx_path, txt_path)
            print(f"Converted: {filename} → {txt_filename}")


folder_path = './Yoruba_Translated_docx'
convert_all_docx_in_folder(folder_path)
