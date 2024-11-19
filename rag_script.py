import PyPDF2
from langchain.text_splitter import CharacterTextSplitter
from sentence_transformers import SentenceTransformer
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

from langchain_ollama import OllamaEmbeddings
from langchain.chat_models import ollama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_ollama import ChatOllama
from langchain.schema import AIMessage, HumanMessage
from langchain import LangChain, VectorStoreRetriever, ConversationBufferMemory, ConversationChain 
from ollama import Ollama

# Text Extraction from the web
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  

ollama_model = ChatOllama(model="llama3", server="http://localhost:11434")

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

def database(chunks,embeddings):
    
    vector_store = FAISS.from_texts(texts=chunks, embedding=embedding_model)
    docs = faiss_index.similarity_search("What is  Encoder and Decoder Stacks?", k=2)
    return vector_store.tolist()

def conversational_retrieval_with_ollama(vector_store, ollama_model, query):
    docs = vector_store.similarity_search(query, k=2)
    context = "\n".join([doc.page_content for doc in docs])  # Combine retrieved documents
    
    # Create a prompt
    prompt = f"The following context is provided:\n{context}\n\n{query}"
    
    # Query Ollama
    response = ollama_model.chat(prompt)
    return response
