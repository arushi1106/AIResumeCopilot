import json
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_resume(resume_json):
    prompt = f"""
Analyze the following resume as if you are a Senior Hiring Manager at a top AI company.

Evaluate the resume on a scale of 0–100.

Scoring Guidelines:
- 90–100: Outstanding resume, interview-ready.
- 80–89: Strong resume with only minor improvements needed.
- 70–79: Good resume but several areas need strengthening.
- 60–69: Average resume with noticeable gaps.
- Below 60: Weak resume requiring major improvements.

Be honest and critical.

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