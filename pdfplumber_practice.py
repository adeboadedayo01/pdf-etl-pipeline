import pdfplumber #type: ignore

# Open the PDF
with pdfplumber.open("/Users/apple/Downloads/Introductory_Statistics_2e_-_WEB.pdf") as pdf:
    
    # Opening page 101, it has a frequency table
    page = pdf.pages[100]  
    
    chars = page.chars    # individual characters pdfplumber can see
    words = page.extract_words()   # words pdfplumber can see
    text = page.extract_text() 

    print(f"Characters found: {len(chars)}")
    print(f"Words found: {len(words)}")
    print(f"Text length: {len(text) if text else 0}")