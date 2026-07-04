# AI Job Application Copilot

An AI-powered autonomous job search platform that analyzes a candidate's CV, discovers relevant live job opportunities, tailors application materials using Large Language Models (LLMs), and manages the entire application lifecycle with human-in-the-loop approval.

The goal is to automate the repetitive parts of job hunting while ensuring every application remains personalized, accurate, and under the user's control.

---

# Tech Stack

- Python
- FastAPI
- OpenAI API / Llama 3
- LangChain
- LangGraph
- Qdrant Vector Database
- Sentence Transformers
- PostgreSQL
- Playwright
- Docker

---

# Project Architecture

```
                CV (PDF)
                    │
                    ▼
            PDF Text Extraction
                    │
                    ▼
           Structured CV Parser
                    │
                    ▼
        Embedding Generation
                    │
                    ▼
          Qdrant Vector Database
                    │
                    ▼
          Job Search Agent
                    │
                    ▼
        Semantic Job Matching
                    │
                    ▼
      Resume Tailoring Agent
                    │
                    ▼
      Cover Letter Generation
                    │
                    ▼
      Human Review & Approval
                    │
                    ▼
          Automated Application
                    │
                    ▼
      Application Tracker Dashboard
```

---

# Features

## CV Processing

- Upload PDF resumes
- Extract text from resumes
- Parse structured candidate information
- Identify skills, education, experience, certifications, and projects

---

## Intelligent Job Discovery

- Search live job openings
- Collect jobs from multiple job boards
- Filter based on:
  - Skills
  - Experience
  - Location
  - Visa sponsorship
  - Salary
  - Remote/Hybrid preferences

---

## AI Resume Optimization

- Tailor resume for every job description
- Highlight relevant skills
- Rewrite bullet points
- Optimize ATS score

---

## AI Cover Letter Generator

- Personalized cover letters
- Company-specific customization
- Role-specific customization

---

## Human-in-the-loop Approval

Every generated resume and cover letter is reviewed by the user before submission.

No application is submitted automatically without explicit approval.

---

## Automated Job Applications

- Login securely
- Fill application forms
- Upload tailored documents
- Submit applications
- Track submission status

---

## Application Tracker

Maintain a centralized dashboard showing

- Applied
- Interview
- Assessment
- Rejected
- Offer
- Withdrawn

---

# Development Roadmap

## ✅ Phase 1 — CV Upload & Parsing

Completed

- FastAPI backend
- PDF upload endpoint
- Resume storage
- PDF text extraction using PyPDF

Current API:

```
POST /upload
```

Response:

```json
{
  "filename": "resume.pdf",
  "text": "Extracted CV text..."
}
```

---

## Phase 2 — AI Resume Parser

- Extract candidate name
- Email
- Phone
- Skills
- Experience
- Education
- Projects
- Certifications

Output:

```json
{
    "name": "...",
    "skills": [...],
    "experience": [...],
    "education": [...]
}
```

---

## Phase 3 — Embeddings & Vector Database

- Sentence Transformers
- OpenAI Embeddings
- Chunking
- Store embeddings in Qdrant
- Semantic retrieval

---

## Phase 4 — RAG Pipeline

Ask questions about the resume:

- Does this candidate know LangGraph?
- What cloud experience does the candidate have?
- Summarize AI projects.

---

## Phase 5 — Live Job Search

Search jobs from:

- LinkedIn
- Greenhouse
- Ashby
- Lever
- Workday
- Company career pages

---

## Phase 6 — Job Matching Engine

Calculate a compatibility score using

- Skill overlap
- Experience
- Education
- Location
- Visa sponsorship
- Salary preferences

---

## Phase 7 — Resume Tailoring Agent

Generate a customized resume for each job posting.

---

## Phase 8 — Cover Letter Agent

Generate personalized cover letters aligned with the company and role.

---

## Phase 9 — Application Agent

Automate application submission using browser automation while requiring user approval before final submission.

---

## Phase 10 — Application Dashboard

Track

- Applied jobs
- Interview invitations
- Assessments
- Offers
- Rejections

---

# Current Progress

## Completed

- FastAPI backend
- Resume upload endpoint
- PDF parsing
- Text extraction
- API documentation with Swagger

Example:

```
CV.pdf
    │
    ▼
FastAPI
    │
    ▼
Save PDF
    │
    ▼
PyPDF
    │
    ▼
Extract Text
    │
    ▼
JSON Response
```

---

# Future Improvements

- Multi-agent architecture using LangGraph
- Memory-enabled agents
- Resume versioning
- Interview preparation agent
- Recruiter email generator
- AI networking assistant
- Job recommendation dashboard
- Analytics and insights
- Docker deployment
- Cloud deployment (AWS/GCP/Azure)

---

# Project Status

🚧 In Active Development

Current milestone:

✅ Resume Upload & Text Extraction

Next milestone:

➡️ AI-powered Structured Resume Parsing