import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.pinecone import Pinecone
from langchain.document_loaders import TextLoader

INDEX_NAME = "arep-ia"
FILES = ["ingenieria-electronica.txt", "ingenieria-civil.txt", "ingenieria-sistemas.txt", "ingenieria-electrica.txt",
         "economia.txt", "ingenieria-industrial.txt"]


def load_context():
    # Connect to the PineCone DataBase
    pinecone.init(api_key="709f5a01-aa44-4eb6-8ad2-e81bcae0afc0", environment="gcp-starter")
    # Object that turns text into a 1536 dimension vector
    embeddings = OpenAIEmbeddings()
    # Get the PineCone Index where we are going to store our context
    Pinecone.from_existing_index(INDEX_NAME, embeddings)
    for i in FILES:
        text = load_text(f"./context/{i}")
        # Upload the contents of the file to the index using the embedding created
        Pinecone.from_texts(texts=[text], embedding=embeddings, index_name=INDEX_NAME)


# Get raw text of the file
def load_text(file):
    loader = TextLoader(file, encoding="utf8")
    documents = loader.load()
    text_splitter = CharacterTextSplitter()
    docs = text_splitter.split_documents(documents)
    return docs[0].page_content
