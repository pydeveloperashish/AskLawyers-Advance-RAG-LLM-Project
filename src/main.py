from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from data_retrieval import get_retriever
from dotenv import load_dotenv, find_dotenv
import os 


app = FastAPI()
templates = Jinja2Templates(directory="../templates")

# Mount static files
app.mount("/static", StaticFiles(directory="../static"), name="static")


retriever = get_retriever()

custom_template = """
You are an helpful assistent of law. Answer query in detail

{context}

{question}
"""

prompt = PromptTemplate(template=custom_template, input_variables=["context", "question"])

llm = ChatOpenAI(model="gpt-3.5-turbo-0125")



def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt},
)

@app.get("/", response_class=HTMLResponse)
async def get_data(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def post_data(request: Request, Input: str = Form(...)):
    response = qa_chain.invoke(Input)
    data = {"message": response['result']}
    return templates.TemplateResponse("index.html", {"request": request, "data": data})