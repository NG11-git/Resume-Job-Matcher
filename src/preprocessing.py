import re


def clean_text(text: str) -> str:
    
    if not text:
        return ""
    
    # Convert to lowercase
    text = text.lower()

    # Remove emails and phone numbers

    text = re.sub(r"\S+@\S+", " ", text)
    text = re.sub(r"\+?\d[\d -]{8,}\d", " ", text)

    # Remove special characters and numbers
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Replace multiple spaces/newlines with singles spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text
