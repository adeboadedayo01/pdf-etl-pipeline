 # OpenStax PDF ETL Experiments

 This repository contains small experimental scripts for extracting and analyzing text from the **Introductory Statistics 2e (OpenStax)** PDF.  
 The goal is to compare different tools (PyPDF, pdfplumber, Tesseract OCR, pdf2image) for tasks like finding specific sections and reading table data.

 ## Features

 - **PyPDF text extraction**
   - Inspect basic PDF metadata and page count.
   - Find pages containing `"Key Terms"`.
   - Save matches to a structured JSON file.

 - **pdfplumber inspection**
   - Check whether `pdfplumber` can see characters, words, and text on a specific page.

 - **Tesseract OCR + pdf2image**
   - Convert a PDF page to a high‑resolution PNG.
   - Run Tesseract OCR on the page.
   - Experiment with image pre‑processing (grayscale, sharpening) to improve OCR.
   - Compare OCR results with PyPDF’s native text extraction on the same page.

 ## Project Structure

 - `pypdf_practice.py`  
   - Opens the PDF with `pypdf.PdfReader`.
   - Prints title and number of pages.
   - Scans all pages and prints a short preview of pages that contain `"Key Terms"`, counting how many pages match.

 - `pypdf_extract.py`  
   - Similar search for `"Key Terms"`, but instead of printing everything, it:
     - Collects matches in a list of `{ "page_number", "preview" }`.
     - Writes results to `output.json`.

 - `pdfplumber_practice.py`  
   - Opens the same PDF with `pdfplumber`.
   - Inspects **page 101** (index `100`).
   - Prints:
     - Number of characters `pdfplumber` can see.
     - Number of words `pdfplumber` can see.
     - Length of extracted text (if any).
   - Demonstrates that `pdfplumber` cannot read that specific page (likely because it is rendered as an image/table).

 - `tesseract_practice.py`  
   - Uses `pdf2image.convert_from_path` to turn **page 101** into a PNG (`page101.png`).
   - Saves the image locally so you can visually inspect how the page looks.

 - `tesseract_extract.py`  
   - Converts page 101 to an image with `pdf2image`.
   - Runs `pytesseract.image_to_string` directly on the image.
   - Prints the text Tesseract was able to extract (note: table data is imperfect).

 - `tesseract_update.py`  
   - Converts page 101 to an image.
   - Applies simple pre‑processing:
     - Converts to grayscale.
     - Sharpens the image.
   - Saves the processed image as `page101_processed.png`.
   - Runs Tesseract on the processed image and prints the extracted text.
   - Uses `pypdf.PdfReader` to extract text from the same page and prints a preview, noting that `pypdf` did a better job for the table in this case.

 ## Requirements

 ### Python packages

 Install dependencies (preferably in a virtual environment):

 ```bash
 pip install pdf2image pytesseract Pillow pypdf pdfplumber
 ```

 ### System dependencies

 Some tools require external binaries:

 - **Poppler** (for `pdf2image`)
   - macOS (Homebrew):

     ```bash
     brew install poppler
     ```

 - **Tesseract OCR** (for `pytesseract`)
   - macOS (Homebrew):

     ```bash
     brew install tesseract
     ```

 Make sure these are available on your `PATH` before running the scripts.

 ## Configuration

 All scripts assume the input PDF is located at:

 ```text
 /Users/apple/Downloads/Introductory_Statistics_2e_-_WEB.pdf
 ```

 To use a different path:

 1. Open the script you’re running (e.g. `pypdf_practice.py`).
 2. Change the string passed to `pypdf.PdfReader(...)`, `pdfplumber.open(...)`, or `convert_from_path(...)` to your own file path.

 Example:

 ```python
 PDF_PATH = "/path/to/your/file.pdf"
 reader = pypdf.PdfReader(PDF_PATH)
 ```

 ## How to Run

 From the project directory, run any script with Python:

 ```bash
 python pypdf_practice.py        # Scan for "Key Terms" and print matches
 python pypdf_extract.py         # Save summary of "Key Terms" pages to output.json
 python pdfplumber_practice.py   # Inspect what pdfplumber sees on page 101
 python tesseract_practice.py    # Export page 101 as page101.png
 python tesseract_extract.py     # Basic Tesseract OCR on page 101
 python tesseract_update.py      # Pre-processed Tesseract OCR + pypdf comparison
 ```

 Generated artifacts:

 - `output.json` – JSON list of pages containing `"Key Terms"` (from `pypdf_extract.py`).
 - `page101.png` – Raw image of page 101 (from `tesseract_practice.py`).
 - `page101_processed.png` – Pre‑processed image of page 101 (from `tesseract_update.py`).

 ## Notes and Next Steps

 - These scripts are intended as **learning experiments** around PDF ETL, not production‑ready tools.
 - Possible improvements:
   - Parameterize the PDF path and search term (e.g. via command‑line arguments).
   - Add error handling when the PDF is missing or unreadable.
   - Turn repeated logic (e.g. scanning pages for a keyword) into reusable functions.
