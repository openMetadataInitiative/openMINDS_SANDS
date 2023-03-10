import requests
from bs4 import BeautifulSoup

# URL of the website containing the table
url = 'https://meca-brain.org/software/marsatlas/'

# Make a request to the website and get the HTML content
response = requests.get(url)
html_content = response.content

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all table elements on the page
tables = soup.find_all('table')

# Loop through each table and search for the one you want
for table in tables:
    # Check if the table has the attributes or contents you are looking for
    if table.has_attr('class') and 'example-table' in table['class']:
        # Print the contents of the table
        print(table)
