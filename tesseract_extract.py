from pdf2image import convert_from_path #type: ignore
import pytesseract #type: ignore

# Converting page 101 to an image
print("Converting page 101 to image...")

images = convert_from_path(
    "/Users/apple/Downloads/Introductory_Statistics_2e_-_WEB.pdf",
    dpi=300,          # quality of the image - 300 is good
    first_page=101,   # start at page 101
    last_page=101     # stop at page 101
)

# Running Tesseract OCR on the image
print("Reading text from image...")

text = pytesseract.image_to_string(images[0])

print("--- TEXT EXTRACTED BY TESSERACT ---")
print(text)

# data on the table wasn't recorded appropriately