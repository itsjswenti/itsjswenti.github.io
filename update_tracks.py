#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

# Read the new tracklist
with open('tracklist_new.txt', 'r', encoding='utf-8') as f:
    tracklist = f.read().strip()

# Read the current HTML file
with open('index.html', 'r', encoding='utf-8-sig') as f:
    html = f.read()

# Replace the tracks array using regex
pattern = r'tracks: \[[\s\S]*?\],'
replacement = f"tracks: [\n{tracklist}\n  ],"
html = re.sub(pattern, replacement, html)

# Write back with proper UTF-8 encoding (without BOM this time)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with 191 tracks")
