from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("sample.docx")
print(result.text_content)