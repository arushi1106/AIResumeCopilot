import json
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
schema = {
    "score": 0,
    "evaluation": {
        "technical_skills": {
            "score": 0,
            "comment": ""
        },
        "experience": {
            "score": 0,
            "comment": ""
        },
        "projects": {
            "score": 0,
            "comment": ""
        },
        "education": {
            "score": 0,
            "comment": ""
        },
        "business_impact": {
            "score": 0,
            "comment": ""
        },
        "resume_quality": {
            "score": 0,
            "comment": ""
        }
    },
    "strengths": [],
    "weaknesses": [],
    "missing_skills": [],
    "recommendations": [],
    "summary": ""
}

def analyze_resume(resume_json):
    prompt = f"""
You are a Senior AI Hiring Manager with over 15 years of experience recruiting Machine Learning, NLP, LLM, and Software Engineers at companies such as OpenAI, Google DeepMind, Anthropic, and Microsoft.

Evaluate the resume objectively.

Score the resume from 0–100 based on:
- Technical skills
- Relevant experience
- Projects
- Education
- Business impact
- Resume quality and clarity

Be constructive but honest.


For each category provide:
- score (0–100)
- short comment (1–3 sentences)

Return ONLY valid JSON matching this schema:

{json.dumps(schema, indent=2)}

Resume:

{json.dumps(resume_json, indent=2)}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert recruiter."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    result = response.choices[0].message.content

    return json.loads(result)