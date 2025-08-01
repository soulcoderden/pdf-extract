from core.worker import process_pdf_file

def main():
    """Main function that processes a PDF and prints both original and filtered duration lines."""
    
    # PDF file to process
    target_pdf = "20250731090635_Avenue-Supermarts_31072025_Motilal-Oswal.pdf"
    
    # Process the PDF file
    result = process_pdf_file(target_pdf)
    
    # Print original lines (without sentence filtering)
    print("=== ORIGINAL DURATION LINES (No Sentence Filtering) ===")
    print(f"Total lines found: {len(result['original'])}")
    print("-" * 60)
    for i, line in enumerate(result['original'], 1):
        print(f"{i}. \"{line}\"")
    
    print("\n" + "="*80 + "\n")
    
    # Print filtered lines (with sentence filtering)
    print("=== FILTERED DURATION LINES (With Sentence Filtering) ===")
    print(f"Total lines found: {len(result['filtered'])}")
    print("-" * 60)
    for i, line in enumerate(result['filtered'], 1):
        print(f"{i}. \"{line}\"")
    
    print(f"\nFiltering removed {len(result['original']) - len(result['filtered'])} lines")

if __name__ == "__main__":
    main() 