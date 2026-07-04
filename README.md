# AI Job Application Copilot

An AI-powered autonomous job search platform that analyzes a candidate's resume, evaluates its quality, matches it against job descriptions, identifies skill gaps, tailors application materials using Large Language Models (LLMs), and manages the complete job application lifecycle with human-in-the-loop approval.

The platform automates repetitive aspects of job hunting while ensuring every recommendation remains personalized, transparent, and under the user's control.

---

# Features

## AI Resume Processing

- Upload PDF resumes
- Extract resume text using PyMuPDF
- Parse resumes into structured JSON using GPT-4.1-mini
- Extract:
  - Personal Information
  - Skills
  - Work Experience
  - Education
  - Projects
  - Certifications

---

## AI Resume Evaluation

Evaluate resumes as an experienced AI hiring manager.

Provides:

- Overall Resume Score (0–100)
- Technical Skills Score
- Experience Score
- Projects Score
- Education Score
- Business Impact Score
- Resume Quality Score

Additionally generates:

- Recruiter Comments
- Strengths
- Weaknesses
- Missing Skills
- Improvement Recommendations
- Professional Resume Summary

---

## AI Job Matching

Compare any resume against a job description.

Provides:

- Overall Match Score (0–100)
- Skill Match Score
- Experience Match Score
- Education Match Score
- Keyword Match Score
- Matched Skills
- Missing Skills
- Skill Gap Analysis
- Hiring Recommendation
- Confidence Level
- Personalized Recommendations
- Job Match Summary

---

## Planned Features

- Resume Tailoring
- ATS Optimization
- Cover Letter Generation
- Interview Preparation
- Job Search Agent
- Automated Job Applications
- Application Dashboard
- Resume Chatbot (RAG)

---

# Tech Stack

### Backend

- Python
- FastAPI

### AI

- OpenAI GPT-4.1-mini
- LangChain
- LangGraph

### Vector Search

- Qdrant
- Sentence Transformers

### Database

- PostgreSQL

### Automation

- Playwright

### Deployment

- Docker

---

# Project Architecture

```
                         Resume PDF
                              │
                              ▼
                    PDF Text Extraction
                              │
                              ▼
                   AI Resume Parser (LLM)
                              │
                              ▼
                    Structured Resume JSON
                     │                    │
                     │                    │
                     ▼                    ▼
             Resume Evaluation      Job Description
                     │                    │
                     │                    ▼
                     │            AI Job Matcher
                     │                    │
                     ▼                    ▼
           Resume Analysis       Match Analysis
                     │                    │
                     └────────────┬───────┘
                                  ▼
                      Resume Improvement Agent
                                  │
                                  ▼
                       Tailored Resume Generator
                                  │
                                  ▼
                     Cover Letter Generator
                                  │
                                  ▼
                       Human Review & Approval
                                  │
                                  ▼
                    Automated Job Application
                                  │
                                  ▼
                      Application Tracker
```

---

# REST API

## Upload & Parse Resume

```
POST /upload
```

Uploads a PDF resume and returns:

- Extracted Resume JSON
- AI Resume Evaluation

---

## Job Matching

```
POST /job-match
```

Inputs:

- Resume PDF
- Job Description

Returns:

- Match Score
- Skill Gap Analysis
- Missing Skills
- Hiring Recommendation
- Improvement Suggestions

---

# Current Progress

## ✅ Phase 1 — Resume Upload & Parsing

Completed

- PDF Upload
- Resume Storage
- Text Extraction using PyMuPDF
- Structured Resume Parsing using GPT-4.1-mini
- JSON Resume Generation
- FastAPI Endpoint
- Swagger Documentation

---

## ✅ Phase 2 — AI Resume Evaluation

Completed

- Resume Review
- Overall Score
- Category-wise Evaluation
- Recruiter Comments
- Strengths
- Weaknesses
- Missing Skills
- Personalized Recommendations
- Resume Summary

---

## ✅ Phase 3 — AI Job Matching

Completed

- Resume vs Job Description Matching
- Overall Match Score
- Skill Match Analysis
- Experience Match Analysis
- Education Match Analysis
- Keyword Match Analysis
- Matched Skills
- Missing Skills
- Skill Gap Detection
- Hiring Recommendation
- Confidence Score
- Personalized Recommendations
- AI Match Summary

---

# Upcoming Roadmap

## 🚀 Phase 4 — AI Resume Tailoring

- Resume Rewrite
- ATS Optimization
- Bullet Point Enhancement
- Keyword Optimization
- Role-specific Resume Generation

---

## 🚀 Phase 5 — Cover Letter Generator

- Company-specific Cover Letters
- Role-specific Cover Letters
- Personalized Writing Style

---

## 🚀 Phase 6 — ATS Optimization

- ATS Compatibility Score
- Keyword Density Analysis
- Formatting Suggestions
- Section Completeness Analysis

---

## 🚀 Phase 7 — Resume Knowledge Base (RAG)

- Resume Embeddings
- Qdrant Integration
- Semantic Search
- Resume Chatbot

Example:

```
What cloud technologies does this candidate know?

Summarize all NLP experience.

Which projects use Docker?
```

---

## 🚀 Phase 8 — Live Job Search

Supported Sources

- LinkedIn
- Greenhouse
- Lever
- Ashby
- Workday
- Company Career Pages

---

## 🚀 Phase 9 — AI Job Application Agent

- Browser Automation
- Resume Upload
- Cover Letter Upload
- Form Filling
- Human Approval Before Submission

---

## 🚀 Phase 10 — Application Dashboard

Track

- Saved Jobs
- Applied Jobs
- Assessments
- Interviews
- Rejections
- Offers
- Application Status Timeline

---

# Example Workflow

```
Resume PDF
     │
     ▼
Upload
     │
     ▼
Extract Text
     │
     ▼
AI Resume Parser
     │
     ▼
Resume JSON
     │
     ├───────────────┐
     ▼               ▼
Resume Review    Job Matching
     │               │
     └──────┬────────┘
            ▼
Resume Tailoring
            │
            ▼
Cover Letter
            │
            ▼
Application Agent
            │
            ▼
Dashboard
```

---

# Future Improvements

- Multi-Agent Architecture using LangGraph
- Memory-enabled AI Agents
- Resume Versioning
- Recruiter Email Generator
- Networking Assistant
- AI Career Coach
- Interview Simulator
- Analytics Dashboard
- Docker Deployment
- AWS Deployment
- Azure Deployment
- GCP Deployment

---

# Project Status

🚧 **Actively Under Development**

Current Completion:

- ✅ Resume Parsing
- ✅ AI Resume Review
- ✅ AI Job Matching
- 🚧 Resume Tailoring
- 🚧 ATS Optimization
- 🚧 Cover Letter Generation
- 🚧 RAG Resume Chat
- 🚧 Job Search Agent
- 🚧 Application Automation
- 🚧 Frontend Dashboard

---