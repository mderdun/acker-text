import xml.etree.ElementTree as ET
import os
import json
import nltk
import re

# If missing, download the punkt package
nltk.download('punkt')

# Create a dictionary to store the paragraphs for each XML file
paragraphs_dict = {}

# List of subfolders where XML files are located
subfolders = ["blackTarantula", "sources"]

# Iterate over subfolders and XML files
for subfolder in subfolders:
    folder_path = os.path.join('xml', subfolder)
    for filename in os.listdir(folder_path):
        if filename.endswith('.xml'):
            # Parse XML
            tree = ET.parse(os.path.join(folder_path, filename))
            root = tree.getroot()
            paragraphs = []

            # Get all text from div with type text, other than head tags
            paragraph_text = []
            for div in root.findall('.//{http://www.tei-c.org/ns/1.0}div[@type="text"]//*'):
                if div.tag == '{http://www.tei-c.org/ns/1.0}head':
                    continue
                if div.tag == '{http://www.tei-c.org/ns/1.0}p':
                    paragraph = " ".join(paragraph_text).strip()
                    if paragraph:
                        paragraphs.append(paragraph)
                    paragraph_text = []
                if div.text is not None:
                    paragraph_text.append(div.text)

            # Add the last paragraph if it exists
            if paragraph_text:
                paragraph = " ".join(paragraph_text).strip()
                if paragraph:
                    paragraphs.append(paragraph)

            # Add the paragraphs to the dictionary
            # Remove .xml extension from filename
            filename_without_extension = os.path.splitext(filename)[0]
            paragraphs_dict[filename_without_extension] = paragraphs

# Write the dictionary to a JSON file and save to the xml folder
with open('xml/paragraphs.json', 'w') as fp:
    json.dump(paragraphs_dict, fp, indent=2)
