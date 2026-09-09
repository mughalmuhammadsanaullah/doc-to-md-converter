from pathlib import Path
from markitdown import MarkItDown, MarkItDownException

md = MarkItDown()
SUPPORTED_EXTENSIONS = {".docx", ".pdf", ".xlsx"}

def convert_to_markdown(file_path):
    extension = Path(file_path).suffix.lower()
    if extension not in SUPPORTED_EXTENSIONS:
        print(f"Error: '{extension}' is not supported. Supported types: {', '.join(sorted(SUPPORTED_EXTENSIONS))}")
        return None

    try:
        result = md.convert(file_path)
        return result.text_content
    except FileNotFoundError:
        print(f"Error: no file found at '{file_path}'.")
        return None
    except MarkItDownException as e:
        print(f"Error: couldn't convert '{file_path}' — it may be corrupted or unsupported.\nDetails: {e}")
        return None