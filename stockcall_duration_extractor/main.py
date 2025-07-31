from pathlib import Path

from extractor.pdf_handler import extract_text_from_pdf


def main():
    pdf_path = Path(__file__).parent / "data" / "example.pdf"
    output_path = Path(__file__).parent / "outputs" / "extracted_text.txt"

    text = extract_text_from_pdf(str(pdf_path))

    # Print the first 500 characters
    print(text[:500])

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
