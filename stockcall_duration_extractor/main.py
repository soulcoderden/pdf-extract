from pathlib import Path

from extractor.pdf_handler import extract_text_from_pdf
from extractor.text_cleaner import segment_sentences
from rule_engine import match_duration_patterns


def main():
    pdf_path = Path(__file__).parent / "data" / "example.pdf"
    output_path = Path(__file__).parent / "outputs" / "extracted_text.txt"

    text = extract_text_from_pdf(str(pdf_path))

    # Split into sentences and print with line numbers
    sentences = segment_sentences(text)
    for idx, sentence in enumerate(sentences, start=1):
        print(f"{idx:>3}: {sentence}")

    match = match_duration_patterns(sentences)
    if match:
        print("Match found:", match)
    else:
        print("No match found")

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
