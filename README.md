# AI Job Application Copilot

An AI-powered autonomous job search platform that analyzes a candidate's resume, evaluates their profile like an experienced recruiter, discovers relevant live job opportunities, tailors application materials using Large Language Models (LLMs), and manages the job application lifecycle with human-in-the-loop approval.

The goal is to automate the repetitive parts of job hunting while ensuring every application remains personalized, accurate, and under the user's control.

---

# Tech Stack

- Python
- FastAPI
- OpenAI GPT-4.1-mini
- LangChain *(Upcoming)*
- LangGraph *(Upcoming)*
- Qdrant Vector Database *(Upcoming)*
- Sentence Transformers *(Upcoming)*
- PostgreSQL *(Upcoming)*
- Playwright *(Upcoming)*
- Docker *(Upcoming)*

---

# Project Architecture

```
                   Resume (PDF)
                        │
                        ▼
              PDF Text Extraction
                        │
                        ▼
          AI Structured Resume Parser
                        │
                        ▼
          Structured Resume JSON
                        │
                        ▼
            AI Resume Evaluation
                        │
                        ▼
        Resume Score & Feedback
                        │
                        ▼
        Embedding Generation (Upcoming)
                        │
                        ▼
        Semantic Job Matching (Upcoming)
                        │
                        ▼
        Resume Tailoring Agent
                        │
                        ▼
      AI Cover Letter Generator
                        │
                        ▼
      Human Review & Approval
                        │
                        ▼
     Automated Job Applications
                        │
                        ▼
      Application Tracker Dashboard
```

---

# Features

## Resume Processing

- Upload PDF resumes
- Extract text using PyMuPDF
- AI-powered structured resume parsing
- Convert resumes into structured JSON
- Extract:
  - Personal Information
  - Skills
  - Experience
  - Education
  - Projects
  - Certifications

---

## AI Resume Evaluation

Evaluate resumes like an experienced hiring manager.

Includes:

- Overall Resume Score (0–100)
- Technical Skills Score
- Experience Score
- Projects Score
- Education Score
- Business Impact Score
- Resume Quality Score

Along with:

- Detailed recruiter comments
- Strengths
- Weaknesses
- Missing Skills
- Personalized recommendations
- Professional resume summary

---

## Intelligent Job Discovery *(Upcoming)*

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

## AI Resume Optimization *(Upcoming)*

- Tailor resumes for every job description
- Rewrite bullet points
- Highlight relevant experience
- Improve ATS compatibility

---

## AI Cover Letter Generator *(Upcoming)*

- Personalized cover letters
- Company-specific customization
- Role-specific customization

---

## Human-in-the-loop Approval *(Upcoming)*

Every generated resume and cover letter is reviewed by the user before submission.

No application is submitted automatically without explicit approval.

---

## Automated Job Applications *(Upcoming)*

- Secure login
- Fill application forms
- Upload tailored documents
- Submit applications
- Track application status

---

## Application Dashboard *(Upcoming)*

Track every application from one place.

- Applied
- Interviews
- Assessments
- Offers
- Rejections
- Withdrawn

---

# Development Roadmap

## ✅ Phase 1 — Resume Upload & Text Extraction

Completed

- FastAPI backend
- PDF upload endpoint
- Resume storage
- PDF text extraction using PyMuPDF

---

## ✅ Phase 2 — AI Resume Parser

Completed

Extracts:

- Name
- Email
- Phone
- LinkedIn
- GitHub
- Skills
- Experience
- Education
- Projects
- Certifications

Returns structured JSON.

---

## ✅ Phase 3 — AI Resume Evaluation

Completed

Provides:

- Overall resume score (0–100)
- Technical skills evaluation
- Experience evaluation
- Projects evaluation
- Education evaluation
- Business impact evaluation
- Resume quality evaluation
- Recruiter comments
- Strengths
- Weaknesses
- Missing skills
- Recommendations
- Resume summary

---

## 🚧 Phase 4 — Resume Embeddings

Planned

- Sentence Transformers
- OpenAI Embeddings
- Resume chunking
- Vector storage in Qdrant

---

## 🚧 Phase 5 — Resume RAG Assistant

Ask questions about any uploaded resume.

Example:

- What cloud technologies does this candidate know?
- Summarize the AI projects.
- Does this candidate have leadership experience?

---

## 🚧 Phase 6 — Live Job Search Agent

Search jobs from:

- LinkedIn
- Greenhouse
- Ashby
- Lever
- Workday
- Company Career Pages

---

## 🚧 Phase 7 — AI Job Matching

Calculate compatibility based on:

- Skills
- Experience
- Education
- Visa sponsorship
- Location
- Salary
- Seniority

---

## 🚧 Phase 8 — Resume Tailoring Agent

Generate a customized resume for each job.

---

## 🚧 Phase 9 — AI Cover Letter Agent

Generate personalized cover letters.

---

## 🚧 Phase 10 — Job Application Agent

Automate applications using Playwright while requiring user approval before submission.

---

## 🚧 Phase 11 — Job Application Dashboard

Track:

- Applications
- Interviews
- Assessments
- Rejections
- Offers

---

# Current Progress

## ✅ Completed

- FastAPI backend
- Resume upload API
- PDF text extraction
- AI resume parser
- Structured JSON generation
- AI recruiter-style resume evaluation
- Resume scoring (0–100)
- Category-wise evaluation
- Recruiter feedback generation
- Swagger API documentation

Current workflow:

```
Resume (PDF)
      │
      ▼
FastAPI Upload
      │
      ▼
PyMuPDF Text Extraction
      │
      ▼
GPT-4.1 Resume Parser
      │
      ▼
Structured Resume JSON
      │
      ▼
GPT-4.1 Resume Evaluator
      │
      ▼
Resume Score
      │
      ▼
Strengths
Weaknesses
Recommendations
Summary
```

---

# Future Improvements

- ATS Compatibility Score
- Resume vs Job Description Matching
- Skill Gap Detection
- Resume Rewrite Suggestions
- AI Bullet Point Optimization
- Interview Question Generator
- AI Recruiter Chat
- Resume Version Comparison
- Resume Version History
- Multi-agent Architecture with LangGraph
- Memory-enabled Agents
- Docker Deployment
- AWS/GCP/Azure Deployment

---

# Project Status

🚧 **Active Development**

## ✅ Completed

### Resume Processing

- ✔ PDF Resume Upload
- ✔ Resume Text Extraction (PyMuPDF)
- ✔ AI Resume Parsing
- ✔ Structured Resume JSON

### Resume Evaluation

- ✔ Overall Resume Score (0–100)
- ✔ Technical Skills Evaluation
- ✔ Experience Evaluation
- ✔ Projects Evaluation
- ✔ Education Evaluation
- ✔ Business Impact Evaluation
- ✔ Resume Quality Evaluation
- ✔ Recruiter Comments
- ✔ Strengths & Weaknesses Detection
- ✔ Missing Skills Detection
- ✔ Personalized Recommendations
- ✔ Professional Resume Summary

---

## 🚀 Next Milestone

### AI Job Matching Engine

Upcoming features:

- Semantic Resume Search
- Resume Embeddings
- Vector Database (Qdrant)
- Job Description Matching
- ATS Compatibility Analysis
- Resume Tailoring
- Cover Letter Generation
- Live Job Search
- Automated Job Applications
- Application Dashboard