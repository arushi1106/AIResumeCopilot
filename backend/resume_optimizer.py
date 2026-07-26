import json
from openai_client import client, parse_llm_json

schema = {
    "tailoring_summary": "",

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
    "tailoring_changes": {
    "professional_summary": "",
    "skills": [],
    "experience": [],
    "projects": []
},

"missing_requirements": [
    {
        "requirement": "",
        "reason": ""
    }
],

"validation": {
    "fabrication_detected": False,
    "companies_modified": False,
    "job_titles_modified": False,
    "dates_modified": False
},

    "interview_readiness": {
        "score": 0,
        "comment": ""
    },

    "tailored_resume": {
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


def tailor_resume(resume_json, job_description):

    prompt = f"""
You are an expert ATS evaluator, Senior AI Resume Coach, Career Consultant, and Hiring Manager with over 15 years of experience hiring AI Engineers, Machine Learning Engineers, NLP Engineers, Data Scientists, and Software Engineers at companies including OpenAI, Anthropic, Google DeepMind, Microsoft, Meta, Amazon, Apple and NVIDIA.

Your primary objective is to tailor the candidate's resume specifically for the supplied job description while preserving complete factual accuracy.

Tailoring means:

• Rewrite the Professional Summary to align with the target role.

• Reorder the Skills section based on the importance of technologies requested in the job description.

• Rewrite experience bullet points using stronger action verbs while preserving factual accuracy.

• Rewrite project descriptions to emphasise the technologies and achievements most relevant to the target role.

• Reorder projects based on relevance.

• Improve ATS keyword alignment using ONLY keywords that already exist or are clearly demonstrated within the resume.

• Preserve all existing resume sections.

• Never invent experience, technologies, certifications, achievements or measurable results.

Never fabricate any information.
Return ONLY valid JSON matching the following schema.

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

preserve them inside tailored_resume.

5. Never remove information unless it is duplicated.

6. Never claim experience with technologies that are not already demonstrated.

7. Keywords from the job description may only be added if they truthfully reflect the candidate's existing experience.

8. Reorder skills according to the job description.

9. Reorder projects according to the job description.

10. Rewrite only the Professional Summary, Experience bullets and Project descriptions.

11. Do not modify Education, Certifications, Awards, Publications, Languages or Volunteering unless correcting grammar.

12. If the job description contains technologies, certifications, tools, programming languages, cloud platforms or experience that are not demonstrated in the resume:

• Do NOT add them.

• Add them to missing_requirements.

• Explain why they are missing.

13. Every field in the JSON schema must be returned.

If a value is unknown, use:

""
[]
0

Never omit any field.

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

1. Analyse the job description.

2. Estimate ATS score BEFORE tailoring.

3. Tailor the resume specifically for the supplied job description.

4. Rewrite:
- Professional Summary
- Experience bullet points
- Project descriptions

5. Reorder:
- Skills
- Projects

6. Preserve:
- Education
- Certifications
- Awards
- Publications
- Languages
- Volunteering

7. Estimate ATS score AFTER tailoring.

8. Score:
- Keywords
- Technical Skills
- Experience
- Projects
- Education
- Formatting
- Readability

9. Identify:
- matched keywords
- keywords added
- missing keywords

10. List job requirements that are missing from the resume under missing_requirements.

11. Populate tailoring_changes explaining exactly what changed in each section.

12. Populate validation confirming no factual information was fabricated.

13. Explain every important modification in changes_made.

14. Generate recruiter feedback.

15. Generate interview questions.

16. Return ONLY valid JSON.

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
            f"Resume tailoring failed: {str(e)}"
        ) from e