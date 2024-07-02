import boto3
from langchain_community.retrievers import AmazonKendraRetriever



def get_retriever():
    retriever =  AmazonKendraRetriever(
    index_id="99a9ffbd-4e42-40a4-883a-35c2f6e40301",
    top_k=3,
    region_name="us-east-1")
    return retriever