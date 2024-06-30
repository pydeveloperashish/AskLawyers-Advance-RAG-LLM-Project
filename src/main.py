from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv, find_dotenv
from langchain import hub
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

import os
load_dotenv(find_dotenv())

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize OpenAI embeddings and FAISS vector store
embeddings = OpenAIEmbeddings(api_key = os.getenv('OPENAI_API_KEY'))
vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever()

# Define RAG pipeline setup
# Prompt
prompt = hub.pull("rlm/rag-prompt")

# LLM
llm = ChatOpenAI(api_key = os.getenv('OPENAI_API_KEY'), model_name="gpt-3.5-turbo", temperature=0)

# Post-processing function
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Chain setup
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

@app.get("/", response_class=HTMLResponse)
async def get_data(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def post_data(request: Request, Input: str = Form(...)):
    result = rag_chain.invoke(Input)
    data = {"message": result}
    return templates.TemplateResponse("index.html", {"request": request, "data": data})
