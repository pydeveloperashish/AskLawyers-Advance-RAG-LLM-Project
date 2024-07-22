import boto3
import pandas as pd
from langchain_community.retrievers import AmazonKendraRetriever
import re

def get_retriever():
    retriever = AmazonKendraRetriever(
    index_id="99a9ffbd-4e42-40a4-883a-35c2f6e40301",
    top_k=5,
    region_name="us-east-1")
    return retriever

def get_excerpt(query):
    retriever = get_retriever()
    docs = retriever.invoke(query)
    excerpt_list = []
    for doc in docs:
        excerpt_list.append(doc.metadata['excerpt'])
    return excerpt_list


# excerpts = get_excerpt("what is indian panel code?")
# print(excerpts)

# # Create a pandas DataFrame with the excerpts
# df = pd.DataFrame(excerpts, columns=["Excerpt"])
# # Save the DataFrame to an Excel file
# df.to_excel("../excerpts.xlsx", index=True)
# print("Excerpts saved to ../excerpts.xlsx")