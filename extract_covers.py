#!/usr/bin/env python3
"""
Extract cover art from MP3 files and save to covers folder
"""
import os
from pathlib import Path
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC

# Directories
music_dir = Path("./music")
covers_dir = Path("./covers")
covers_dir.mkdir(exist_ok=True)

print("Extracting cover art from MP3 files...")

for mp3_file in music_dir.glob("*.mp3"):
    try:
        # Get filename without extension
        filename = mp3_file.stem
        cover_path = covers_dir / f"{filename}.jpg"
        
        # Skip if cover already exists
        if cover_path.exists():
            print(f"  ✓ {filename} (already exists)")
            continue
        
        # Try to extract cover art
        audio = MP3(mp3_file, ID3=ID3)
        
        # Look for album art in ID3 tags
        found_cover = False
        for tag in audio.tags.values():
            if isinstance(tag, APIC):
                # Save the cover art
                with open(cover_path, 'wb') as img:
                    img.write(tag.data)
                print(f"  ✓ {filename}")
                found_cover = True
                break
        
        if not found_cover:
            print(f"  ✗ {filename} (no embedded art)")
            
    except Exception as e:
        print(f"  ✗ {filename} (error: {e})")

print("\nDone! Cover art extracted to ./covers/")
print("Note: Files without embedded art will not have covers.")
