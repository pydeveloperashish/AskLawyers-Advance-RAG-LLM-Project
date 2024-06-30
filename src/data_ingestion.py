from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma, FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

#### INDEXING ####
# Load Documents
loader = PyPDFLoader(r'./dataset/Indian Penal Code Book (2).pdf')
docs = loader.load()

# Split
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
print("splits: \n", splits)
# Embed
vectorstore = FAISS.from_documents(documents=splits, 
 embedding=OpenAIEmbeddings())

vectorstore.save_local('faiss_index')
print("DB got saved in local")