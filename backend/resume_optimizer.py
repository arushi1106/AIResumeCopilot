import json
from openai_client import client, parse_llm_json

schema = {
    "resume_summary": "",

    "ats_score_before": 0,
    "ats_score_after": 0,

    "ats_breakdown": {
        "keywords": 0,
        "technical_skills": 0,
        "experience": 0,
        "projects": 0,
        "education": 0,
        "formatting": 0,
        "readability": 0
    },

    "matched_keywords": [],
    "keywords_added": [],
    "keywords_missing": [],

    "resume_strengths": [],
    "resume_weaknesses": [],

    "ats_risks": [
        {
            "risk": "",
            "severity": "Low",
            "recommendation": ""
        }
    ],

    "priority_improvements": [],

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
        ],
        "education": [],
        "certifications": [],
        "awards": [],
        "publications": [], 
        "languages": [],
        "volunteering": []
    },

    "changes_made": [
        {
            "section": "",
            "original": "",
            "improved": "",
            "reason": ""
        }
    ],

    "section_scores": {
        "summary": {
            "score": 0,
            "comment": ""
        },
        "skills": {
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
        }
    },

    "likely_interview_questions": [
        {
    "category": "",
    "difficulty": "",
    "question": "",
    "reason": ""
}
    ],

    "recruiter_decision": {
        "overall_rating": 0,
        "hire_probability": 0,
        "decision": "",
        "confidence_level": "",
        "comment": ""
    },

    "analysis_confidence": 0,

    "final_recruiter_feedback": ""
}


def optimize_resume(resume_json, job_description):

    prompt = f"""
You are an expert ATS evaluator, Senior AI Resume Coach, Career Consultant, and Hiring Manager with over 15 years of experience hiring AI Engineers, Machine Learning Engineers, NLP Engineers, Data Scientists, and Software Engineers at companies including OpenAI, Anthropic, Google DeepMind, Microsoft, Meta, Amazon, Apple and NVIDIA.

Your task is to analyse the candidate's resume against the supplied job description and optimise it while preserving complete factual accuracy.

Return ONLY valid JSON matching the schema below.

{json.dumps(schema, indent=2)}

====================================================
IMPORTANT RULES
====================================================

1. Never invent:
- work experience
- projects
- certifications
- achievements
- technical skills
- responsibilities
- measurable results

2. Never modify:
- employment dates
- company names
- job titles
- university names
- degree names

3. Rewrite bullet points ONLY to:
- improve grammar
- improve readability
- improve ATS optimisation
- improve recruiter appeal
- strengthen wording

4. Preserve every existing resume section.

If the resume contains:
- certifications
- awards
- volunteering
- publications
- languages

preserve them inside optimized_resume.

5. Never remove information unless it is duplicated.

6. Never claim experience with technologies that are not already demonstrated.

7. Keywords from the job description may only be added if they truthfully reflect the candidate's existing experience.

8. Every field in the JSON schema must be returned.

If unknown use:

""
[]
0

Never omit fields.

9. Return ONLY JSON.

Do NOT include:
- Markdown
- Triple backticks
- Explanations
- Notes
- Introductory text
- Closing remarks

====================================================
TASKS
====================================================

1. Write a concise professional resume summary.

2. Estimate ATS score BEFORE optimisation.

3. Optimise the resume.

4. Estimate ATS score AFTER optimisation.

5. Score:
- Keywords
- Technical Skills
- Experience
- Projects
- Education
- Formatting
- Readability

6. Identify:
- matched keywords
- added keywords
- missing keywords

7. Identify:
- resume strengths
- resume weaknesses

8. Identify ATS risks.

For each risk provide:
- risk
- severity
- recommendation

9. Recommend the five highest priority improvements.

10. Explain every important modification in "changes_made".

11. Score each resume section and explain why.

12. Estimate interview readiness.

13. Generate five personalised interview questions.

Each question must include:
- question
- reason

14. Act as a hiring manager and provide:

overall_rating (0-10)

hire_probability (0-100)

decision:
- Strong Interview
- Interview
- Borderline
- Reject

confidence_level:
- High
- Medium
- Low

comment

15. Estimate your confidence in the analysis (0-100).

16. Finish with concise recruiter feedback (2-4 sentences).

====================================================
SCORING GUIDE
====================================================

90-100 = Excellent

80-89 = Strong

70-79 = Competitive

60-69 = Average

Below 60 = Needs Improvement

====================================================
RESUME
====================================================

{json.dumps(resume_json, indent=2)}

====================================================
JOB DESCRIPTION
====================================================

{job_description}
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            temperature=0.1,
            max_completion_tokens=5000,
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert ATS evaluator, "
                        "Senior Recruiter, "
                        "Resume Writer and Hiring Manager.\n"
                        "Always return ONLY valid JSON."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return parse_llm_json(
            response.choices[0].message.content
        )

    except Exception as e:
        raise RuntimeError(
            f"Resume optimisation failed: {str(e)}"
        ) from e