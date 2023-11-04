
import re

# Read in the text file
with open('xml/bio/mcbride.txt', 'r') as f:
    text = f.readlines()

# Remove empty lines and lines beginning with '***'
text = [line.strip() for line in text if line.strip() and not line.startswith('***')]

# Find the indices of the lines beginning with 'CHAPTER '
chapter_indices = [i for i, line in enumerate(text) if line.startswith('CHAPTER ')]

# Add the final index to the list
chapter_indices.append(len(text))

# Create the TEI XML
xml = '<TEI>\n'
for i in range(len(chapter_indices) - 1):
    start = chapter_indices[i]
    end = chapter_indices[i+1]
    chapter_text = '\n'.join(text[start:end])
    chapter_text = chapter_text.split('\n')
    chapter_xml = f'<div type="chapter" n="{i+2}">\n' # add n value to the tag
    for j in range(len(chapter_text)):
        if chapter_text[j].strip() != '':
            if j % 2 == 0:
                chapter_xml += f'<p>{chapter_text[j]}</p>\n'
            else:
                chapter_xml += f'<p>{chapter_text[j]}</p>\n'
    chapter_xml += '</div>\n'
    xml += chapter_xml
xml += '</TEI>'

# Write the XML to a file
with open('output.xml', 'w') as f:
    f.write(xml)
