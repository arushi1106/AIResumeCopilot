from openai_client import client, parse_llm_json

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
        temperature=0,
        response_format={"type": "json_object"},
    )

    return parse_llm_json(response.choices[0].message.content)