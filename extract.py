import pypdf #type: ignore
import json

reader = pypdf.PdfReader("/Users/apple/Downloads/Introductory_Statistics_2e_-_WEB.pdf")

# Store results in a list instead of just printing
results = []

for i in range(len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()

    if text and "Key Terms" in text:
        results.append({
            "page_number": i + 1,
            "preview": text[:50]
        })

# Save the list to a JSON file
with open("output.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"Done! Found {len(results)} pages. Saved to output.json")