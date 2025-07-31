# PDF Extract

This project demonstrates extracting duration expressions from PDF text using [spaCy](https://spacy.io/).

## Installation

1. Create a Python environment and activate it.
2. Install the project requirements, including spaCy:

```bash
pip install spacy
```

3. Download the small English model used by the scripts:

```bash
python -m spacy download en_core_web_sm
```

## Segmenting Sentences

The function `segment_sentences(text)` splits PDF text into sentences using spaCy's language model. The model handles common punctuation as well as newlines often found in PDF extraction. Given a block of text it returns a list of clean sentence strings.

## Finding Duration Expressions

`match_duration_patterns(doc)` scans a spaCy `Doc` object for patterns describing durations such as "12 months" or "3-5 years". It uses spaCy's rule matcher to detect number/measurement combinations. The matcher returns spans corresponding to these expressions so they can be highlighted or logged.

## Example

Running `main.py` processes an input file and prints detected durations. For example:

```bash
python main.py sample.pdf
```

Sample output when a match is found:

```
Found duration: "12 months" at page 2
```

This indicates the text "12 months" was extracted and matched on the second page of the PDF.
