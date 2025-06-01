import openai
from config import API_KEY, ENDPOINT

def classify_ticket(text):
    openai.api_key = API_KEY
    openai.api_base = ENDPOINT
    response = openai.ChatCompletion.create(
        engine='gpt-4o',
        messages=[
            {'role': 'system', 'content': 'Classify the IT support issue.'},
            {'role': 'user', 'content': f'{text}'}
        ]
    )
    return response['choices'][0]['message']['content'].strip()