import fitz  

def extract_text_from_pdf(file_obj):
    text = ""
    with fitz.open(stream=file_obj.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text
