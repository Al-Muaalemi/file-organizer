#!/usr/bin/env python3
"""File Organizer - Sort files into folders by extension."""

import argparse
import os
import shutil

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".md"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Code": [".py", ".js", ".ts", ".html", ".css", ".java", ".cpp", ".c", ".go", ".rs"],
    "Others": [],
}


def get_category(ext: str) -> str:
    for category, extensions in CATEGORIES.items():
        if ext.lower() in extensions:
            return category
    return "Others"


def organize(directory: str, dry_run: bool = False) -> None:
    """Move files into categorized subfolders."""
    for fname in os.listdir(directory):
        fpath = os.path.join(directory, fname)
        if not os.path.isfile(fpath):
            continue
        _, ext = os.path.splitext(fname)
        category = get_category(ext)
        dest_dir = os.path.join(directory, category)
        dest = os.path.join(dest_dir, fname)
        print(f"{'[dry-run] ' if dry_run else ''}Moving {fname} -> {category}/")
        if not dry_run:
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(fpath, dest)


def main():
    parser = argparse.ArgumentParser(description="Organize files by type")
    parser.add_argument("directory", help="Directory to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview without moving files")
    args = parser.parse_args()
    organize(args.directory, args.dry_run)


if __name__ == "__main__":
    main()
