import re

text = "Chapter 1 Sampling and Data"

# Search for the word "Chapter" in the text
result = re.search("Data", text)

if result:
    print("Found it!")
    print(result)
else:
    print("Not found")