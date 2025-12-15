import re, argparse
from .explorer import explore

def main():
    # command line arguments
    parser = argparse.ArgumentParser(description="File explorer CLI")
    parser.add_argument("--format", type=str, choices=["txt", "xlsx"], default="txt", help="Output format (txt or xlsx)")
    parser.add_argument("--ext", type=str, default=None, help="Desired extension of collected files")
    parser.add_argument("--fname", type=str, default="file_list", help="Desired name for output file")
    # parse input arguments
    args = parser.parse_args()
    # Validate desired file name
    if not re.match(r"^[\w\-]+$", args.fname):
        parser.error("Invalid file name")
    # call explorer to find all files in directory
    file_list = explore(extension=args.ext)
    if args.format == "txt":
        with open(f"{args.fname}.txt", "w", encoding="utf-8") as output_file:
            for item in file_list:
                output_file.write(item.name + "\n")
    elif args.format == "xlsx":
        # import package to create Excel output
        import openpyxl
        # Write Excel output
        wbook = openpyxl.Workbook()
        sheet = wbook.active
        for row, item in enumerate(file_list, start=1):
            sheet[f"A{row}"] = item.name
        wbook.save(filename=f"{args.fname}.xlsx")