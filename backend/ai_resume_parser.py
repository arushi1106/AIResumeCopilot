import json
from openai_client import client

def parse_resume(text):

    prompt = f"""
    You are an expert resume parser.

    Extract:

    - name
    - email
    - phone
    - location
    - linkedin profile
    - github profile
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

    result = response.choices[0].message.content
    return json.loads(result)