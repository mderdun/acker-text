import xml.etree.ElementTree as ET
import os
import json
import nltk
import re
from nltk.tokenize import sent_tokenize

#If missing, download the punkt package
nltk.download('punkt')

#Create a dictionary to store the sentences for each XML file
sentences_dict = {}

#Iterate over all XML files in the xml folder
for filename in os.listdir('xml'):
    if filename.endswith('.xml'):
        #Parse XML
        tree = ET.parse(os.path.join('xml', filename))
        root = tree.getroot()
        string = ""
        result = []

        #Get all text from div with type text, other than head tags
        for div in root.findall('.//{http://www.tei-c.org/ns/1.0}div[@type="text"]//*'):
            if div.tag == '{http://www.tei-c.org/ns/1.0}head':
                continue
            # removing all empty nodes
            if div.text is None :
               div.text = ''
            string += str(div.text) + " "
            result = "".join(string) 

        #Sentence Tokenize and add to list
        sentences = sent_tokenize(str(result))

        #Remove all empty strings
        sentences = list(filter(None, sentences))

        #Remove all newlines
        sentences = [re.sub(r'\n', '', sentence) for sentence in sentences]

        #Add the sentences to the dictionary
        # Remove .xml extension from filename
        filename_without_extension = os.path.splitext(filename)[0]
        sentences_dict[filename_without_extension] = sentences

#Write the dictionary to a JSON file and save to the xml folder
with open('xml/sentences.json', 'w') as fp:
    json.dump(sentences_dict, fp)
