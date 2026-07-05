import json
from openai_client import client


def match_resume_to_job(resume_json, job_description):

    prompt = f"""
You are a Senior AI Hiring Manager with over 15 years of experience hiring AI Engineers, Machine Learning Engineers, NLP Engineers, LLM Engineers, AI Researchers, and Software Engineers at companies such as OpenAI, Anthropic, Google DeepMind, Microsoft, Meta, and Amazon.

Your task is to objectively evaluate how well the candidate's resume matches the provided job description.

Evaluate the candidate exactly as you would during an initial resume screening.

Base your assessment on:

• Technical skill alignment
• Relevant industry experience
• Project relevance
• Business impact
• Education
• Evidence of production-ready engineering
• Cloud & deployment experience
• AI/LLM experience
• ATS keyword alignment
• Overall suitability for the role

Be fair, objective, and constructive.

Do NOT inflate scores.

Scoring Guidelines:

90–100
Outstanding candidate. Strong interview recommendation with only minor gaps.

80–89
Strong candidate with a few noticeable gaps but likely worth interviewing.

70–79
Reasonable match. Would require discussion depending on applicant pool.

60–69
Weak match. Several important gaps.

Below 60
Poor match. Missing many required qualifications.

Return ONLY valid JSON using this schema:

{{
  "match_score": 0,

  "evaluation": {{
    "technical_skills": {{
      "score": 0,
      "comment": ""
    }},
    "experience": {{
      "score": 0,
      "comment": ""
    }},
    "projects": {{
      "score": 0,
      "comment": ""
    }},
    "education": {{
      "score": 0,
      "comment": ""
    }},
    "business_impact": {{
      "score": 0,
      "comment": ""
    }},
    "ats_alignment": {{
      "score": 0,
      "comment": ""
    }}
  }},

  "matched_skills": [],

  "missing_skills": [],

  "strengths": [],

  "weaknesses": [],

  "recommendations": [],

  "interview_recommendation": "",

  "confidence": "",

  "summary": ""
}}

Rules:

- Scores must be between 0 and 100.
- Comments should be concise (2–4 sentences).
- Only include skills that explicitly appear in both the resume and the job description under matched_skills.
- missing_skills should contain important missing requirements from the job description.
- Recommendations should be specific and actionable.
- interview_recommendation must be one of:
  - "Strong Yes"
  - "Yes"
  - "Maybe"
  - "No"
- confidence must be one of:
  - "High"
  - "Medium"
  - "Low"
- summary should explain why the candidate is or isn't a good fit in one concise paragraph.

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