import re
import yaml
import spacy
from pathlib import Path

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def load_patterns() -> list[str]:
    """
    Load regex patterns from YAML file.
    
    Returns:
        list[str]: List of regex patterns
    """
    patterns_file = Path(__file__).parent.parent / "patterns" / "duration_patterns.yaml"
    
    with open(patterns_file, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    
    return [item['pattern'] for item in data['patterns']]

def is_valid_sentence(line: str) -> bool:
    """
    Check if a line is a valid English sentence using hybrid approach.
    
    Args:
        line (str): Line to validate
        
    Returns:
        bool: True if line is a valid sentence
    """
    # Skip lines that are too short
    if len(line.strip()) < 20:
        return False
    
    # Skip lines that are just fiscal years (e.g., "FY25 FY26e FY27e")
    if re.match(r'^[\s]*FY\d{2,4}[eE]?[\s]*$', line.strip()):
        return False
    
    # Skip lines that are just repeated fiscal years
    if re.match(r'^(FY\d{2,4}[eE]?\s*)+$', line.strip()):
        return False
    
    # Skip lines that start with bullet points
    if re.match(r'^[◼•▪▫◦‣⁃]\s*', line.strip()):
        return False
    
    # Skip lines that end with incomplete phrases (like "- Q2")
    if re.search(r'-\s*[A-Z]\d$', line.strip()):
        return False
    
    # Skip specific header patterns
    if re.match(r'^Q\d\s+FY\d{2,4}\s+results?\s+analysis$', line.strip(), re.IGNORECASE):
        return False
    
    # Use spaCy to analyze the sentence
    doc = nlp(line.strip())
    
    # Skip if spaCy doesn't recognize it as a sentence
    if len(doc) < 3:  # Too few tokens
        return False
    
    # Check if it has a verb (using spaCy's POS tagging)
    has_verb = any(token.pos_ == "VERB" for token in doc)
    
    # For financial text, we want to be more lenient
    # Accept lines that have verbs OR are meaningful financial statements
    
    # Check for financial keywords that indicate meaningful content
    financial_keywords = ['expect', 'target', 'maintain', 'retain', 'guide', 'forecast', 'project', 'estimate', 'plan', 'likely', 'expected', 'commenced', 'reduced', 'covering', 'valued', 'on-boarded', 'results', 'analysis', 'quarter', 'below', 'estimates', 'revenue', 'earnings', 'growth', 'margin', 'capex', 'debt', 'order', 'guidance', 'outlook', 'valuation']
    
    has_financial_content = any(keyword in line.lower() for keyword in financial_keywords)
    
    # Accept if it has a verb OR has meaningful financial content
    if not has_verb and not has_financial_content:
        return False
    
    # Skip if it's just a list or enumeration (too many nouns compared to verbs)
    noun_count = len([token for token in doc if token.pos_ in ["NOUN", "PROPN"]])
    verb_count = len([token for token in doc if token.pos_ == "VERB"])
    if noun_count > verb_count * 5:  # Very lenient ratio for financial text
        return False
    
    # Skip if it's just a header (starts with proper noun and is very short)
    if doc[0].pos_ == "PROPN" and len(doc) <= 3:
        return False
    
    return True

def find_duration_lines(lines: list[str]) -> list[str]:
    """
    Find lines containing duration data for stock recommendations.
    
    Args:
        lines (list[str]): List of text lines to search
        
    Returns:
        list[str]: List of unique lines containing duration data
    """
    
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
        
        # Skip lines that are not valid sentences
        if not is_valid_sentence(line):
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