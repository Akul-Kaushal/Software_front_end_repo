import PyPDF2
from langchain.text_splitter import CharacterTextSplitter
from sentence_transformers import SentenceTransformer


# Text Extraction from the web
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=200,
        chunk_overlap=40,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def create_embedding(text_chunk,embedding_model):
    """Generate an embedding for a text chunk using a preloaded model."""
    embedding = embedding_model.encode(text_chunk)
    return embedding.tolist()  # Convert to list for JSON compatibility

def