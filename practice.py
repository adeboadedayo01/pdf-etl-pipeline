import pypdf #type: ignore

# Open the PDF file
reader = pypdf.PdfReader("/Users/apple/Downloads/Introductory_Statistics_2e_-_WEB.pdf")

# Print some stats about the PDF and the first page
print("Title:", reader.metadata.title)
print("Number of pages:", len(reader.pages))
print("First page:", reader.pages[0].extract_text())