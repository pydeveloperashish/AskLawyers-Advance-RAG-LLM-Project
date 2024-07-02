from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from data_retrieval import get_retriever
import os 

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

response = qa_chain.invoke("What is sections in IPC?")
print(response['result'])