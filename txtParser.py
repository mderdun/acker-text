
with open('xml/bio/mcbride.txt', 'r') as f:
    lines = f.readlines()

filtered_lines = [line for line in lines if line.strip() and not line.startswith('CHAPTER ') and not line.startswith('* * *')]

with open('output.txt', 'w') as f:
    f.writelines(filtered_lines)
