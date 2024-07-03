from src.prompt_templates import ENHANCED_QUERY_PROMPT_TEMPLATE
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os

# Load the .env file
load_dotenv()

# Get the API key from the .env file
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

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