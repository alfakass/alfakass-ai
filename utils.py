import pymupdf 

def simple_test_splitter(text: str, chunk_size: int =10, overlap: int = 0) -> list[str]:
    chunks = []

    for i in range(0, len(text), chunk_size):
        if i == 0:
            chunks.append(text[i-0:i+chunk_size])
            continue
        chunks.append(text[i-overlap:i+chunk_size])
    
    return chunks

def pdf_to_text() -> str:
    text = ""
    document = pymupdf.open("documents/Afakass_LLC_Code_of_Conduct.pdf")

    for page in document:
        text += page.get_text()
    
    return text