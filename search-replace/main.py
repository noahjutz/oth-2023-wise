import os
import time
import re

BBOX_PATTERN = r"\\bbox\[(\w*),?\w*\]"
COLORBOX_PATTERN = r"\\colorbox{\w*}"
COLORBOX_REPLACE = r"\\colorbox{\g<1>}"

def process(text):
    text = re.sub(BBOX_PATTERN, COLORBOX_REPLACE, text)
    matches = re.finditer(COLORBOX_PATTERN, text)

    insert_c_at = []
    for match in matches:
        stack_size = 0
        i = match.end()
        while True:
            match text[i]:
                case "{":
                    stack_size += 1
                    if stack_size == 1:
                        insert_c_at.append(i+1)
                case "}":
                    stack_size -= 1
                    if stack_size == 0:
                        insert_c_at.append(i)
                        break
            i += 1
        
    offset = 0
    for i in insert_c_at:
        pre = text[:i+offset]
        post = text[i+offset:]
        text = pre + "$" + post
        offset += 1

    return text

mdfiles = []
for root, _, files in os.walk("../vault"):
    for file in files:
        path = os.path.join(root, file)
        if path.endswith(".md"):
            mdfiles.append(path)

contents = []
for file in mdfiles:
    with open(file, 'r') as md:
        contents.append(md.read())

for filename, contents in zip(mdfiles, contents):
    contents = process(contents)
    with open(filename, 'w') as f:
        f.write(contents)

