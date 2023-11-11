import pinecone
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms.openai import OpenAI
from langchain.vectorstores.pinecone import Pinecone

INDEX_NAME = "arep-ia"


def search(query):
    pinecone.init(api_key="709f5a01-aa44-4eb6-8ad2-e81bcae0afc0", environment="gcp-starter")
    embeddings = OpenAIEmbeddings()
    # if you already have an index, you can load it like this
    docsearch = Pinecone.from_existing_index(INDEX_NAME, embeddings)
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="refine", retriever=docsearch.as_retriever(search_type="similarity"))
    return qa.run(query)
