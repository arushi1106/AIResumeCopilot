import json
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_resume(resume_json):
    prompt = f"""
Analyze the following resume.

Pretend you are a senior hiring manager at a top AI company. Tell me honestly what's weak, whats missing, whats good, whats great.

Return ONLY valid JSON.

Return this format:

{{
  "overall_score": 0,
  "strengths": [],
  "weaknesses": [],
  "missing_skills": [],
  "recommendations": [],
  "summary": ""
}}

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