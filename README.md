# AI Job Application Copilot

An AI-powered job application platform that helps candidates optimize every stage of the job search process using Large Language Models (LLMs).

The platform extracts structured information from resumes, evaluates resume quality, compares resumes against job descriptions, identifies skill gaps, generates ATS-optimized resumes, and provides recruiter-style feedback to maximize interview success.

Designed with a **human-in-the-loop** approach, every AI-generated recommendation remains transparent, editable, and under the user's control.

---

# Features

## 📄 AI Resume Processing

- Upload PDF resumes
- Extract text using PyMuPDF
- Parse resumes into structured JSON using GPT-4.1-mini
- Automatically extract:
  - Personal Information
  - Professional Summary
  - Skills
  - Work Experience
  - Education
  - Projects
  - Certifications

---

## 🤖 AI Resume Evaluation

Evaluate resumes like an experienced AI recruiter.

### Generates

- Overall Resume Score (0–100)
- Technical Skills Score
- Experience Score
- Projects Score
- Education Score
- Business Impact Score
- Resume Quality Score

### AI Feedback

- Recruiter Comments
- Resume Strengths
- Resume Weaknesses
- Missing Skills
- Personalized Recommendations
- Professional Resume Summary

---

## 🎯 AI Job Matching

Compare any resume against a job description.

### Generates

- Overall Match Score
- Skill Match Score
- Experience Match Score
- Education Match Score
- Keyword Match Score
- Matched Skills
- Missing Skills
- Skill Gap Analysis
- Hiring Recommendation
- Confidence Score
- AI Match Summary
- Personalized Recommendations

---

## 🚀 AI Resume Tailoring & ATS Optimization

Automatically rewrites resumes to align with a target job description while preserving factual accuracy.

### Features

- ATS Score Before vs After
- ATS Breakdown
  - Keywords
  - Technical Skills
  - Experience
  - Projects
  - Education
  - Formatting
- Interview Readiness Score
- Section-wise Resume Scores
- Strongest Resume Section
- Weakest Resume Section
- Recruiter Hiring Decision
- Overall Candidate Rating
- Hire Probability
- Confidence Score
- Keywords Added
- Missing Keywords
- Resume Improvement Recommendations
- AI-Generated Interview Questions
- Resume Bullet Point Enhancement
- Optimized Professional Summary
- Optimized Experience Section
- Optimized Projects Section
- Final Recruiter Feedback

---

# Tech Stack

## Backend

- Python
- FastAPI

## Frontend

- React
- Vite

## AI

- OpenAI GPT-4.1-mini
- LangChain
- LangGraph

## Vector Database

- Qdrant
- Sentence Transformers

## Database

- PostgreSQL

## Automation

- Playwright

## Deployment

- Docker

---

# Project Architecture

```text
                          Resume PDF
                               │
                               ▼
                    PDF Text Extraction
                               │
                               ▼
                      AI Resume Parser
                               │
                               ▼
                 Structured Resume JSON
             ┌───────────────┼────────────────┐
             ▼               ▼                ▼
     Resume Review     Job Matching    Resume Tailoring
             │               │                │
             └───────┬───────┴────────────────┘
                     ▼
            Recruiter Evaluation
                     ▼
          ATS Optimization Report
                     ▼
       Interview Preparation Assets
                     ▼
        Cover Letter Generation (Planned)
                     ▼
          Human Review & Approval
                     ▼
      Automated Job Application (Planned)
                     ▼
         Application Dashboard (Planned)
```

---

# REST API

## Upload & Parse Resume

```http
POST /upload
```

### Returns

- Parsed Resume JSON
- AI Resume Evaluation

---

## AI Job Matching

```http
POST /job-match
```

### Inputs

- Resume PDF
- Job Description

### Returns

- Match Score
- Skill Gap Analysis
- Missing Skills
- Hiring Recommendation
- Personalized Suggestions

---

## AI Resume Tailoring

```http
POST /optimize-resume
```

### Inputs

- Resume PDF
- Job Description

### Returns

- ATS Score Before & After
- ATS Breakdown
- Section Scores
- Interview Readiness
- Optimized Resume
- Keywords Added
- Missing Keywords
- Resume Improvements
- Recruiter Decision
- Interview Questions
- Final Recruiter Feedback

---

# Current Progress

## ✅ Phase 1 — Resume Parsing

Completed

- PDF Upload
- Resume Storage
- Text Extraction using PyMuPDF
- GPT-4.1 Resume Parsing
- Structured Resume JSON
- FastAPI Endpoints
- Swagger Documentation

---

## ✅ Phase 2 — AI Resume Review

Completed

- Resume Scoring
- Recruiter Evaluation
- Skills Analysis
- Missing Skills Detection
- Resume Summary
- Personalized Recommendations

---

## ✅ Phase 3 — AI Job Matching

Completed

- Resume vs Job Description Matching
- Match Score
- Skill Gap Analysis
- Missing Skills Detection
- Hiring Recommendation
- AI Match Summary

---

## ✅ Phase 4 — AI Resume Tailoring

Completed

- ATS Optimization
- Resume Rewrite
- Bullet Point Enhancement
- Keyword Optimization
- Professional Summary Generation
- Recruiter Hiring Decision
- Interview Readiness Score
- Personalized Interview Questions
- Final Recruiter Feedback

---

# Upcoming Roadmap

## 🚀 Phase 5 — Cover Letter Generator

- Company-specific Cover Letters
- Role-specific Cover Letters
- Personalized Writing Style
- Recruiter Tone Selection

---

## 🚀 Phase 6 — Resume Knowledge Base (RAG)

- Resume Embeddings
- Qdrant Integration
- Semantic Resume Search
- Resume Chatbot

Example Queries

```text
What cloud technologies does this candidate know?

Summarize all NLP experience.

Which projects use Docker?

Generate interview questions for this candidate.
```

---

## 🚀 Phase 7 — Live Job Search

Supported Platforms

- LinkedIn
- Greenhouse
- Lever
- Ashby
- Workday
- Company Career Pages

---

## 🚀 Phase 8 — AI Job Application Agent

- Browser Automation
- Resume Upload
- Cover Letter Upload
- Form Filling
- Human Approval Before Submission

---

## 🚀 Phase 9 — Application Dashboard

Track

- Saved Jobs
- Applied Jobs
- Assessments
- Interviews
- Rejections
- Offers
- Application Timeline

---

# Example Workflow

```text
Resume PDF
     │
     ▼
Upload Resume
     │
     ▼
Extract Text
     │
     ▼
AI Resume Parser
     │
     ▼
Structured Resume JSON
     │
 ┌───┼──────────────────────┐
 ▼   ▼                      ▼
Review Match Resume Tailoring
 │    │                      │
 └────┴──────────────┬───────┘
                     ▼
         Recruiter Evaluation
                     ▼
        ATS Optimization Report
                     ▼
      Interview Preparation Kit
                     ▼
   Cover Letter Generation (Planned)
                     ▼
      Job Application Agent (Planned)
                     ▼
        Application Dashboard
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
- Resume Comparison
- Resume Version History
- Docker Deployment
- AWS Deployment
- Azure Deployment
- GCP Deployment

---

# Project Status

🚧 **Actively Under Development**

## ✅ Completed

- Resume Parsing
- AI Resume Review
- AI Job Matching
- AI Resume Tailoring
- ATS Optimization
- Recruiter Evaluation
- Interview Question Generation

## 🚧 In Progress

- Cover Letter Generation
- Resume Knowledge Base (RAG)
- Job Search Agent
- Application Automation
- React Dashboard
- Multi-Agent Workflow

---

# Highlights

- 📄 AI-powered resume parsing from PDF
- 🤖 Recruiter-style resume evaluation
- 🎯 Intelligent job matching against any job description
- 🚀 AI resume tailoring for specific roles
- 📈 ATS optimization with before/after scoring
- 💡 AI-generated resume improvements
- ❓ Personalized interview question generation
- 👨‍💼 Recruiter hiring decision simulation
- ⚡ FastAPI backend with React frontend
- 🔗 Modular architecture ready for autonomous AI agents

---