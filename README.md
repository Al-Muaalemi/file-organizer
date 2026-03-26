# File Organizer

A Python CLI tool that sorts files in a directory into categorized subfolders (Images, Videos, Documents, etc.).

## Installation

```bash
git clone https://github.com/Al-Muaalemi/file-organizer.git
cd file-organizer
python file_organizer.py --help
```

No external dependencies — uses Python standard library only.

## Usage

Organize a directory:
```bash
python file_organizer.py ~/Downloads
```

Preview without moving anything:
```bash
python file_organizer.py ~/Downloads --dry-run
```

## Categories

| Folder | Extensions |
|--------|-----------|
| Images | jpg, jpeg, png, gif, bmp, svg, webp |
| Videos | mp4, mov, avi, mkv, flv, wmv |
| Audio | mp3, wav, flac, aac, ogg |
| Documents | pdf, doc, docx, xls, xlsx, txt, md |
| Archives | zip, tar, gz, rar, 7z |
| Code | py, js, ts, html, css, java, cpp, go, rs |
| Others | everything else |
