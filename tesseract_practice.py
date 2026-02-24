from pdf2image import convert_from_path #type: ignore

# Step 1: Convert page 101 to an image
print("Converting page 101 to image...")

images = convert_from_path(
    "/Users/apple/Downloads/Introductory_Statistics_2e_-_WEB.pdf",
    dpi=300,          # quality of the image - 300 is good
    first_page=101,   # start at page 101
    last_page=101     # stop at page 101
)

# Saving image in file
images[0].save("page101.png")

print("Done! Open page101.png to see the image.")