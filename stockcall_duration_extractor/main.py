from pathlib import Path

from extractor.pdf_handler import extract_text_from_pdf
from extractor.text_cleaner import segment_sentences
from extractor.rule_engine import match_duration_patterns


def main():
    data_dir = Path(__file__).parent / "data"
    output_dir = Path(__file__).parent / "outputs"
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Get all PDF files in the data directory
    pdf_files = list(data_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in data directory")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s) to process:")
    for pdf_file in pdf_files:
        print(f"  - {pdf_file.name}")
    print()
    
    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")
        print("=" * 50)
        
        try:
            text = extract_text_from_pdf(str(pdf_file))
            
            # Split into sentences and print with line numbers
            sentences = segment_sentences(text)
            for idx, sentence in enumerate(sentences, start=1):
                print(f"{idx:>3}: {sentence}")
            
            match = match_duration_patterns(sentences)
            if match:
                print(f"\nMatch found: {match}")
            else:
                print("\nNo match found")
            
            # Save extracted text to output file
            output_file = output_dir / f"{pdf_file.stem}_extracted.txt"
            output_file.write_text(text, encoding="utf-8")
            print(f"Text saved to: {output_file}")
            
        except Exception as e:
            print(f"Error processing {pdf_file.name}: {e}")
        
        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main() 