#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

# Read the tracklist
with open('tracklist.txt', 'r', encoding='utf-8') as f:
    tracklist = f.read()

# Read the current HTML file (might have encoding issues)
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
except:
    # If UTF-8 fails, try with error handling
    with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
        html = f.read()

# Replace the tracks array using regex
pattern = r'tracks: \[[\s\S]*?\],'
replacement = f"tracks: [\n{tracklist}\n  ],"
html = re.sub(pattern, replacement, html)

# Write back with proper UTF-8 encoding (with BOM to ensure proper encoding)
with open('index.html', 'w', encoding='utf-8-sig') as f:
    f.write(html)

print("Fixed encoding in index.html")
