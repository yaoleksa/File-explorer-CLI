# fexplorer

**Simple File Explorer CLI Tool**

`fexplorer` is a lightweight command-line utility for collecting a list of files in a directory and saving it to a text or Excel file.

---

## 🔹 Features

- Recursively collects files from the current directory  
- Filter files by extension (`--ext`)  
- Output to `.txt` (default) or `.xlsx` (`--format`)  
- Specify custom output file name (`--fname`)  
- Easy to install and use  

---

## 🔹 Installation

```bash
# For local development
pip install -e .

# With Excel support
pip install -e .[xlsx]

---

## 🔹 Installation

Create a text file with all files ```fexplorer```