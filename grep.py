import sys
import re

if len(sys.argv) < 3:
    raise ValueError("Wrong format! Correct format is: grep.py PATTERNS FILE [OPTION...]")

pattern = sys.argv[1]
filename = sys.argv[2]
options = sys.argv[3:]
pattern = pattern.replace("\"", "")
if '-v' in options:
    pattern = "^((?!" + pattern + ").)*$"

text_file = open(filename, 'r')
text = text_file.readlines()

matches = []

if '-ignoreCase' in options:
    reg = re.compile(pattern, re.IGNORECASE)
else:
    reg = re.compile(pattern)

matched_lines = []
for line in text:
    line = line.replace("\n", "")
    match = reg.search(line)
    if match is not None:
        matched_lines.append(line)

if '-count' in options:
    print(len(matched_lines))
else:
    for line in matched_lines:
        print(line)

text_file.close()
