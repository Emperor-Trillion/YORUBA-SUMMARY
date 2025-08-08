import unicodedata

# ✅ Allowed characters (Yoruba + English)
allowed_chars = set(
    "AÁÀEÉÈẸẸ́Ẹ̀IÍÌOÓÒỌỌ́Ọ̀UÚÙ"
    "aáàeéèẹẹ́ẹ̀iíìoóòọọ́ọ̀uúù"
    "Ṣṣ"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    ".,!?;:'\"()[]{}-–—… \n"
)

# 🔄 Optional: map similar characters to Yoruba equivalents
replacement_map = {
    'ç': 'ṣ',
    'ñ': 'n',
    'ã': 'an',
    'õ': 'on',
    'â': 'a',
    'ê': 'e',
    'î': 'i',
    'ô': 'o',
    'û': 'u',
    'ä': 'a',
    'ë': 'e',
    'ï': 'i',
    'ö': 'o',
    'ü': 'u',
    'ÿ': 'i',
    'ž': 'ṣ',
    'ś': 'ṣ',
    ' ': ' ',  # preserve space
    '\n': '\n' # preserve newline
}

def sanitize_text(text):
    result = []
    for char in text:
        if char in allowed_chars:
            result.append(char)
        elif char in replacement_map:
            result.append(replacement_map[char])
        else:
            # Try to normalize and strip accents
            normalized = unicodedata.normalize('NFD', char)
            stripped = ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')
            # If stripped version is allowed, use it
            if stripped in allowed_chars:
                result.append(stripped)
            else:
                # Otherwise, replace with a placeholder or remove
                result.append('')
    return ''.join(result)

# 📂 Read and sanitize file
def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        original_text = f.read()
    cleaned_text = sanitize_text(original_text)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_text)

# 🧪 Example usage
process_file('3_final_segmented_final_merged_output.txt', 'yoruba_cleaned.txt')
