import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract plain text from a local PDF file and return it as a single string.

    Parameters
    ----------
    pdf_path : str
        Path to the PDF file.

    Returns
    -------
    str
        The extracted text content.
    """
    text_parts = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text_parts.append(page.get_text())
    # Join and strip to produce a clean string
    return "\n".join(part.strip() for part in text_parts if part).strip()
