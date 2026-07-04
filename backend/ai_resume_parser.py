from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def parse_resume(text):

    prompt = f"""
    You are an expert resume parser.

    Extract:

    - name
    - email
    - phone
    - skills
    - education
    - experience
    - projects
    - certifications

    Return ONLY valid JSON.

    Resume:

    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content