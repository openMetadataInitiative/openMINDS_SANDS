import requests
import pytesseract
from PIL import Image
import io

url = "https://www.frontiersin.org/files/Articles/33392/fnins-06-00171-HTML/image_m/fnins-06-00171-t002.jpg"

response = requests.get(url)

# Open image from binary data using Pillow
img = Image.open(io.BytesIO(response.content))

# Extract text from the image using pytesseract
text = pytesseract.image_to_string(img)

# Split the text into individual lines
lines = text.splitlines()

# Print the extracted lines
for line in lines:
    print(line)

# Store the extracted lines in a list
lines_list = list(lines)