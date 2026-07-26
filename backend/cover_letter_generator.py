import json
from openai_client import client, parse_llm_json

schema = {
    "cover_letter": "",
    "summary": "",
    "tone": "",
    "word_count": 0,
    "key_strengths": [],
    "important_keywords": []
}


def generate_cover_letter(resume_json, job_description):

    prompt = f"""
You are a Senior Recruiter, Career Coach, and Hiring Manager at OpenAI.

Generate a highly personalised cover letter based ONLY on the candidate's resume
and the supplied job description.

Requirements:

- Professional UK English.
- 300–400 words.
- Tailored specifically to the job description.
- Do NOT invent projects, experience or skills.
- Use only information contained in the resume.
- Include enthusiasm for the role.
- Explain why the candidate is a strong fit.
- End with a professional closing.

Return ONLY valid JSON matching this schema:

{json.dumps(schema, indent=2)}

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
                    "You are an expert recruiter and professional cover letter writer. "
                    "Return ONLY valid JSON."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4,
        response_format={"type": "json_object"},
    )

    return parse_llm_json(response.choices[0].message.content)