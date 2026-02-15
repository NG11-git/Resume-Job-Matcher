import pdfplumber
import pytesseract
from pdf2image import convert_from_path


from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text):
    return model.encode(text)



def extract_text_from_pdf(pdf_path):
    text = ""

    try:
        # First try to extract text using pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text 

        if text.strip():
            return text.strip()
    except Exception as e:
        print(f"Direct text extraction failed: {e}")

    # if direct extraction fails, fallback to OCR for image-based PDFs
    print("Falling back to OCR....")
    try:
        images = convert_from_path(pdf_path)
        for image in images:
            text += pytesseract.image_to_string(image)
    except Exception as e:
        print(f"OCR extraction failed: {e}")

    return text.strip()