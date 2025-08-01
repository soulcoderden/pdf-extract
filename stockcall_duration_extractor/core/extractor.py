import fitz  # PyMuPDF
import spacy
from pathlib import Path

# Load spaCy model for sentence segmentation
nlp = spacy.load("en_core_web_sm")

def extract_pdf_lines(pdf_path: str) -> list[str]:
    """
    Extract all lines from a PDF file using proper sentence segmentation.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        list[str]: List of all text lines from the PDF
    """
    text_parts = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text_parts.append(page.get_text())
    
    # Combine all text
    full_text = "\n".join(part.strip() for part in text_parts if part).strip()
    
    # Use spaCy to properly segment sentences
    doc = nlp(full_text)
    sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]
    
    return sentences 