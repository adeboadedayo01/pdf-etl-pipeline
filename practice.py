import pypdf #type: ignore

# Open the PDF file
reader = pypdf.PdfReader("/Users/apple/Downloads/Introductory_Statistics_2e_-_WEB.pdf")

count = 0

# Print basic info about it
print("Title:", reader.metadata.title)
print("Number of pages:", len(reader.pages))

# Extract text from page 17 (start of Chapter 1)
page = reader.pages[16]  #  Python counts from 0, so page 17 = index 16
text = page.extract_text()

#print("\n--- PAGE 17 TEXT ---")
#print(text)

#for i in range(5):
    #page = reader.pages[i]
    #text = page.extract_text()

    #print(f"\n--- PAGE {i + 1} ---")
    #print(text)

    # Search for pages that mention "Key Terms"
for i in range(len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()

    # Only print if the page contains "Key Terms"
    if text and "Key Terms" in text:
        print(f"\n--- PAGE {i + 1} contains 'Key Terms' ---")
        print(text[:50])
        count += 1 

# Print the total after the loop finishes
print(f"\nTotal pages containing 'Key Terms': {count}")