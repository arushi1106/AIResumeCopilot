import json
from openai_client import client

def optimize_resume(resume_json, job_description):
    prompt = f"""
You are a Senior AI Resume Coach and Hiring Manager with over 15 years of experience hiring AI Engineers, Machine Learning Engineers, NLP Engineers, LLM Engineers, and Software Engineers at companies such as OpenAI, Anthropic, Google DeepMind, Microsoft, and Amazon.

Your task is to optimize the candidate's resume specifically for the provided job description.

Rules:

- Never invent skills.
- Never invent experience.
- Never fabricate achievements.
- Preserve factual accuracy.
- Rewrite content only to improve clarity, impact, and ATS compatibility.
- Prioritize keywords from the job description where they truthfully apply.
- Quantify achievements only if numerical evidence already exists.
- Use strong action verbs.
- Make every bullet concise and achievement-oriented.

First estimate the ATS compatibility before optimization.

Then optimize the resume.

Finally estimate the ATS compatibility after optimization.

Return ONLY valid JSON using this schema:

{{
    "ats_score_before": 0,
    "ats_score_after": 0,

    "executive_summary": "",

    "optimized_summary": "",

    "optimized_experience": [
        {{
            "company": "",
            "title": "",
            "bullets": []
        }}
    ],

    "optimized_projects": [
        {{
            "name": "",
            "description": ""
        }}
    ],

    "keywords_added": [],

    "keywords_missing": [],

    "changes_made": [
        {{
            "section": "",
            "original": "",
            "improved": "",
            "reason": ""
        }}
    ],

    "general_recommendations": [],

    "final_recruiter_feedback": ""
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

