from pathlib import Path
from markitdown import MarkItDown, MarkItDownException
import mammoth
import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

def count_tokens(text):
    return len(encoding.encode(text))

def extract_raw_text(file_path):
    with open(file_path, "rb") as f:
        result = mammoth.extract_raw_text(f)
    return result.value

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

markdown_text = convert_to_markdown("sample.docx")
if markdown_text:
    raw_text = extract_raw_text("sample.docx")
    raw_tokens = count_tokens(raw_text)
    markdown_tokens = count_tokens(markdown_text)

    print(markdown_text)
    print(f"\nRaw text tokens: {raw_tokens}")
    print(f"Markdown tokens: {markdown_tokens}")
    if raw_tokens > 0:
        savings = (raw_tokens - markdown_tokens) / raw_tokens * 100
        print(f"Savings: {savings:.1f}%")