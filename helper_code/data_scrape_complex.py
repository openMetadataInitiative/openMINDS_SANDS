import requests
from bs4 import BeautifulSoup

# URL of the website containing the table
url = 'http://meca-brain.org/software/marsatlas-subcortical/'

# Make a request to the website and get the HTML content
response = requests.get(url)
html_content = response.content

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all table elements on the page
tables = soup.find_all('table')

# Create a dictionary to store the lists for each table
tables_data = {}

# Loop through each table and extract the data from its cells
for index, table in enumerate(tables, 1):
    # Create a list for each column of the table
    num_columns = len(table.find_all('tr')[0].find_all('td'))
    column_lists = [[] for _ in range(num_columns)]

    # Loop through each row and extract the data from its cells
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')

        # Loop through each cell and append its contents to the corresponding column list
        for i in range(num_columns):
            column_lists[i].append(cells[i].text.strip())

    # Store the lists for each table in the dictionary
    tables_data[f"table_{index}"] = column_lists

# Print the contents of each table
for table_name, columns in tables_data.items():
    print(f"Table Name: {table_name}")
    for i, column in enumerate(columns):
        print(f"Column {i+1}: {column}")

