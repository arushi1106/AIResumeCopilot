import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def match_resume_to_job(resume_json, job_description):

    prompt = f"""
    You are a Senior AI Recruiter.

    Compare this resume with the following job description.

    Return ONLY valid JSON.

    {{
      "match_score": 0,
      "matched_skills": [],
      "missing_skills": [],
      "matched_keywords": [],
      "recommendations": [],
      "summary": ""
    }}

    Resume:

    {json.dumps(resume_json, indent=2)}

    Job Description:

    {job_description}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert AI recruiter."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return json.loads(response.choices[0].message.content)