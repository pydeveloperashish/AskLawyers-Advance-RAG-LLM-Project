from langchain.chains import RetrievalQA
from dotenv import load_dotenv, find_dotenv
from data_retrieval import get_retriever
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from query_enhancement import get_enhanced_query

llm = ChatOpenAI(model ="gpt-3.5-turbo-0125")

retriever = get_retriever()

custom_template = """
You are an helpful assistent of law. Answer query in detail

{context}

{question}
"""

prompt = PromptTemplate(template=custom_template, input_variables=["context", "question"])


def generate_answer(query):
    enhanced_query = get_enhanced_query(query)
    print()
    print("enhanced_query: ", enhanced_query)
    qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt},
    )
    response = qa_chain.invoke(enhanced_query)
    return response['result']
