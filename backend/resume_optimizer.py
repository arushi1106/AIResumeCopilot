import json
from openai_client import client, parse_llm_json

schema = {
    "ats_score_before": 0,
    "ats_score_after": 0,
    "ats_breakdown": {
        "keywords": 0,
        "technical_skills": 0,
        "experience": 0,
        "projects": 0,
        "education": 0,
        "formatting": 0
    },
    "interview_readiness": {
        "score": 0,
        "comment": ""
    },
    "optimized_resume": {
        "professional_summary": "",
        "skills": [],
        "experience": [
            {
                "company": "",
                "title": "",
                "bullets": []
            }
        ],
        "projects": [
            {
                "name": "",
                "description": ""
            }
        ]
    },
    "keywords_added": [],
    "keywords_missing": [],
    "changes_made": [
        {
            "section": "",
            "original": "",
            "improved": "",
            "reason": ""
        }
    ],
    "section_scores": {
        "summary": 0,
        "skills": 0,
        "experience": 0,
        "projects": 0,
        "education": 0
    },
    "strongest_section": "",
    "weakest_section": "",
    "recommendations": {
        "must_fix": [],
        "nice_to_have": []
    },
    "likely_interview_questions": [
        {
            "question": "",
            "reason": ""
        }
    ],
    "recruiter_decision": {
        "overall_rating": "0/10",
        "hire_probability": "0%",
        "decision": "",
        "confidence": "",
        "comment": ""
    },
    "final_recruiter_feedback": ""
}


def optimize_resume(resume_json, job_description):

    prompt = f"""
You are a Senior AI Resume Coach, ATS Expert, and Hiring Manager with over 15 years of experience recruiting Machine Learning, NLP, LLM, and Software Engineers at companies such as OpenAI, Anthropic, Google DeepMind, Microsoft, Meta, and Amazon.

Your task is to optimize the candidate's resume specifically for the provided job description.

## Objectives

Return ONLY valid JSON matching this schema.

Rules:

- Never invent experience, projects, certifications, or skills.
- Never change dates, companies, job titles, or education.
- Rewrite bullet points only for clarity, ATS optimization, and recruiter appeal.
- Preserve factual accuracy.
- Add keywords only if they are already supported by the resume or job description.
- Estimate ATS scores realistically.
- Explain every important modification in "changes_made".
- Provide section-wise scores.
- Estimate interview readiness.
- Generate 5 personalized interview questions based on the optimized resume.
- Provide a recruiter hiring decision with:
    1. overall_rating (0–10)
    2. hire_probability (0–100%)
    3. decision (Strong Reject / Reject / Maybe / Interview / Strong Interview)
    4. confidence (Low / Medium / High)
    5. short recruiter comment.
- Finish with concise recruiter feedback (2–4 sentences).

{json.dumps(schema, indent=2)}

Scoring Guidelines

ATS Scores:
90-100 = Excellent
80-89 = Strong
70-79 = Competitive
60-69 = Average
Below 60 = Needs Improvement

Hiring Verdict must be one of:

- Strong Interview
- Interview
- Borderline
- Reject

Confidence must be:

- High
- Medium
- Low

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
                "content": (
                    "You are an expert AI recruiter, ATS evaluator, "
                    "resume writer, and hiring manager. "
                    "Return ONLY valid JSON."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        response_format={"type": "json_object"},
    )

    return parse_llm_json(response.choices[0].message.content)