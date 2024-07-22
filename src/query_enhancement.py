from src.prompt_templates import ENHANCED_QUERY_PROMPT_TEMPLATE
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from utils.utils import get_secret
import os

# api_key = get_secret()

client = OpenAI(api_key = "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")

def get_enhanced_query(query):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": ENHANCED_QUERY_PROMPT_TEMPLATE},
        {"role": "user", "content": query}
    ]
    )
    enhanced_query = completion.choices[0].message.content
    return enhanced_query


# print(get_enhanced_query("What is the Indian Penal Code?"))