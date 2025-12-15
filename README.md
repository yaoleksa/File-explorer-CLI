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
```
---

## 🔹 Usage

### Create a text file with all files 
Open terminal and run the command ```fexplorer```
Generates ```file_list.txt``` with all files in the current directory and subdirectories.
### Create an Excel file 
Open terminal and run the command ```fexplorer --format xlsx```
Generates ```file_list.xlsx``` with all files.
### Filter files by extension
Open terminal and run the command ```fexplorer --ext py```
Collects only files with ```.py``` extension.
### Specify a custom output filename
Open terminal and run the command ```fexplorer --fname my_files```
Generates ```my_files.txt``` or ```my_files.xlsx``` depends on which file extension you use
### Combined example
Open terminal and run the command ```fexplorer --format xlsx --ext py --fname python_files```
Generates ```python_files.xlsx``` containing all ```.py``` files.

## 🔹 CLI Arguments

| Argument   | Type | Default     | Description                                    |
| ---------- | ---- | ----------- | ---------------------------------------------- |
| `--format` | str  | `txt`       | Output file format (`txt` or `xlsx`)           |
| `--ext`    | str  | None        | Filter files by extension (e.g., `py`, `txt`)  |
| `--fname`  | str  | `file_list` | Output file name without extension             |

## 🔹 Requirements

- Python >= 3.9
- For Excel output: openpyxl (```pip install fexplorer[xlsx]```)

## Examples

```
# Simple text file with all files
fexplorer

# Excel file with all files
fexplorer --format xlsx

# Only Python files in Excel
fexplorer --format xlsx --ext py

# Custom output file name
fexplorer --fname my_files

# Combined usage
fexplorer --format xlsx --ext py --fname python_files

```
## License

**MIT**