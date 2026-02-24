from pdf2image import convert_from_path #type: ignore
import pytesseract #type: ignore
from PIL import Image, ImageFilter #type: ignore
import pypdf #type: ignore

# Converting page 101 to an image
print("Converting page 101 to image...")
images = convert_from_path(
    "/Users/apple/Downloads/Introductory_Statistics_2e_-_WEB.pdf",
    dpi=300,
    first_page=101,
    last_page=101
)

img = images[0]

# Pre-processing the image to help Tesseract read it better
print("Pre-processing image...")
img = img.convert("L")              # convert to grayscale
img = img.filter(ImageFilter.SHARPEN)  # sharpen the text

# Saving image
img.save("page101_processed.png")

# Running Tesseract on the cleaned image
print("Reading text from image...")
text = pytesseract.image_to_string(img)

print("--- TEXT EXTRACTED BY TESSERACT ---")
print(text)

# the result was better but didn't quite extract the table data perfectly
#pypdf did this perfectly

print("\n--- SAME PAGE WITH pypdf ---")
reader = pypdf.PdfReader("/Users/apple/Downloads/Introductory_Statistics_2e_-_WEB.pdf")
text = reader.pages[100].extract_text()
print(text[:500])