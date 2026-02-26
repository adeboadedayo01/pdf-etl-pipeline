import re

text = "Chapter 1 Sampling and Data"

# Search for the word "Chapter" in the text
# The \d means "any digit"
result = re.search(r"Chapter (\d+)", text)

if result:
    print("Found:", result.group(0))   # the full match
    print("Chapter number:", result.group(1))  # just the number