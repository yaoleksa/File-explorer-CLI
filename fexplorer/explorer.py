import pathlib

def explore(start_path=".", extension=None):
    root = pathlib.Path(start_path).resolve()

    if extension and not extension.startswith("."):
        extension = "." + extension

    for item in root.rglob("*"):
        if item.is_file():
            if extension is None or item.suffix == extension:
                yield item