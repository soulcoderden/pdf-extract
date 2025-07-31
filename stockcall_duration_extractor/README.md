# stockcall_duration_extractor

This tool extracts text from PDF files. It now also demonstrates sentence segmentation using spaCy and a simple duration pattern matcher.

## Usage

First install the dependencies:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Then run `python main.py` to extract text from `data/example.pdf` and save it to `outputs/extracted_text.txt`.
