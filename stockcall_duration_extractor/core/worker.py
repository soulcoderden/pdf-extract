from pathlib import Path
from .extractor import extract_pdf_lines
from .matcher import find_duration_lines

def process_pdf_file(filename: str) -> dict:
    """
    Process a PDF file to find duration lines.
    
    Args:
        filename (str): Name of the PDF file in the data directory
        
    Returns:
        dict: Dictionary containing both original and filtered duration lines
    """
    # Get the full path to the PDF file
    data_dir = Path(__file__).parent.parent / "data"
    pdf_file = data_dir / filename
    
    if not pdf_file.exists():
        print(f"PDF file not found: {filename}")
        return {"original": [], "filtered": []}
    
    # Step 1: Extract all lines from PDF
    all_lines = extract_pdf_lines(str(pdf_file))
    
    # Step 2: Find duration lines using matcher (original)
    original_duration_lines = find_duration_lines_original(all_lines)
    
    # Step 3: Find duration lines using matcher (with sentence filtering)
    filtered_duration_lines = find_duration_lines(all_lines)
    
    return {
        "original": original_duration_lines,
        "filtered": filtered_duration_lines
    }

def find_duration_lines_original(lines: list[str]) -> list[str]:
    """
    Find duration lines WITHOUT sentence filtering (original approach).
    """
    from .matcher import load_patterns
    import re
    
    # Load patterns from YAML
    patterns = load_patterns()
    
    # Compile patterns for efficiency
    compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    
    # Find matching lines
    matching_lines = []
    
    for line in lines:
        # Skip empty lines or very short lines
        if not line or len(line) < 10:
            continue
            
        # Check if line matches any pattern
        for pattern in compiled_patterns:
            if pattern.search(line):
                # Clean up the line (remove excessive whitespace)
                cleaned_line = ' '.join(line.split())
                if cleaned_line not in matching_lines:
                    matching_lines.append(cleaned_line)
                break  # Found a match, no need to check other patterns
    
    return matching_lines 