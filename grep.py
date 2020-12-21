import sys
import re
import os


def processFile(file):
    text_file = open(file, 'r')
    text = text_file.readlines()
    matched_lines = []
    for line in text:
        line = line.replace("\n", "")
        match = reg.search(line)
        if match is not None:
            matched_lines.append(line)

    if '-count' in options:
        print(file + " " + str(len(matched_lines)))
    else:
        for line in matched_lines:
            print(file + " " + line)

    text_file.close()


def processDirectory(directory):
    files_and_dirs = os.listdir(directory)
    for name in files_and_dirs:
        full_path = directory  + "/" + name
        if os.path.isdir(full_path):
            processDirectory(full_path)
        elif os.path.isfile(full_path):
            processFile(full_path)


if len(sys.argv) < 3:
    raise ValueError("Wrong format! Correct format is: grep.py PATTERNS FILE [OPTION...]")

pattern = sys.argv[1]
pattern = pattern.replace("\"", "")

path = sys.argv[2]
filename = sys.argv[2]

options = sys.argv[3:]
lowercase_options = []
for option in options:
    lowercase_options.append(option.lower())
options = lowercase_options

if '-v' in options:
    pattern = "^((?!" + pattern + ").)*$"

matches = []

if '-ignorecase' in options:
    reg = re.compile(pattern, re.IGNORECASE)
else:
    reg = re.compile(pattern)

if os.path.isdir(path):
    processDirectory(path)
elif os.path.isfile(path):
    processFile(path)

