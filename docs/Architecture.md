# Atlas AI - System Architecture

## 1. Purpose

The purpose of this architecture is to provide a modular, scalable, and maintainable design for Atlas AI.

Instead of placing all application logic into a single file, Atlas is divided into independent components, each responsible for a single task. This modular design makes the system easier to develop, test, debug, and extend as new features are added.

The architecture follows the principle of **Separation of Concerns**, where every component has one clearly defined responsibility.

---

# 2. High-Level Architecture

```text
                    USER
                      │
                      ▼
             ┌────────────────┐
             │   Frontend     │
             │   (Streamlit)  │
             └────────────────┘
                      │
                      ▼
             ┌────────────────┐
             │    FastAPI     │
             │    Backend     │
             └────────────────┘
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 Resume Service   Profile Service   Roadmap Service
      │               │                │
      └───────────────┼────────────────┘
                      ▼
           Recommendation Engine
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
      AI/LLM Services        SQLite Database
```

---

# 3. Components

## 3.1 Frontend (Streamlit)

The frontend is responsible for interacting with the user.

Responsibilities:

* Display the dashboard
* User onboarding
* Resume upload
* Display personalized learning roadmap
* Show progress tracking
* Display recommendations

The frontend does **not** perform business logic or machine learning. It simply collects user input and presents results returned by the backend.

---

## 3.2 Backend (FastAPI)

The backend acts as the communication layer between the frontend and Atlas' internal services.

Responsibilities:

* Receive API requests
* Validate user input
* Route requests to the correct service
* Return processed results to the frontend

The backend should remain lightweight and avoid implementing recommendation logic directly.

---

## 3.3 Resume Service

The Resume Service is responsible for extracting useful information from uploaded resumes.

Responsibilities:

* Read PDF resumes
* Extract text
* Identify skills
* Detect education details
* Detect projects
* Detect work experience
* Pass extracted information to the Profile Service

Future versions may include OCR support for scanned resumes.

---

## 3.4 Profile Service

The Profile Service acts as Atlas' memory.

Responsibilities:

* Store user profile information
* Store career goals
* Maintain skill levels
* Track completed projects
* Track certifications
* Maintain learning progress
* Update user information over time

This service provides a complete representation of the user.

---

## 3.5 Roadmap Service

The Roadmap Service generates personalized learning plans.

Responsibilities:

* Analyze current skill level
* Compare skills with career requirements
* Identify missing skills
* Prioritize learning topics
* Generate a personalized learning roadmap
* Estimate completion timelines

The roadmap adapts as the user's profile evolves.

---

## 3.6 Recommendation Engine

The Recommendation Engine is the core intelligence of Atlas.

Responsibilities:

* Analyze user profile
* Interpret roadmap progress
* Recommend next learning steps
* Suggest projects
* Suggest resources
* Encourage practical actions such as applying for internships or building portfolio projects

Future versions will incorporate advanced AI models to improve recommendation quality.

---

## 3.7 AI/LLM Services

This layer provides advanced AI capabilities.

Possible uses include:

* Resume analysis
* Learning roadmap refinement
* Resource recommendations
* Project suggestions
* Interview question generation
* Personalized explanations

By separating AI services from the rest of the application, Atlas can switch between AI providers without affecting the overall architecture.

---

## 3.8 Database (SQLite)

The database stores all persistent information.

Responsibilities:

* User profiles
* Skills
* Goals
* Projects
* Progress
* Roadmaps
* Recommendation history

The database does not perform business logic. It only stores and retrieves data.

Future versions may migrate from SQLite to PostgreSQL for improved scalability.

---

# 4. Data Flow

The following steps describe how Atlas processes a resume upload:

1. The user uploads a PDF resume through the Streamlit frontend.
2. The frontend sends the resume to the FastAPI backend.
3. The backend forwards the file to the Resume Service.
4. The Resume Service extracts information such as skills, education, projects, and experience.
5. The extracted data is passed to the Profile Service.
6. The Profile Service updates the user's profile in the database.
7. The Roadmap Service analyzes the updated profile and identifies skill gaps.
8. The Recommendation Engine generates personalized recommendations and a learning roadmap.
9. The backend returns the processed results to the frontend.
10. The frontend displays the updated dashboard, roadmap, and recommended next actions to the user.

---

# 5. Architectural Principles

Atlas follows these design principles:

* **Modularity:** Each component has a single responsibility.
* **Scalability:** New services can be added without major redesign.
* **Maintainability:** Components remain independent and easy to modify.
* **Separation of Concerns:** User interface, business logic, AI logic, and data storage remain separate.
* **Extensibility:** Future features such as interview simulations, GitHub integration, and adaptive learning can be added with minimal changes to the existing system.

---

# 6. Future Architecture Enhancements

Future versions of Atlas may include:

* Authentication and user accounts
* GitHub integration
* Learning analytics
* Interview simulator
* Coding challenge evaluation
* Notification system
* Cloud database
* Docker deployment
* CI/CD pipeline
* Multi-user support
* Mobile application
* Advanced recommendation models using embeddings and Retrieval-Augmented Generation (RAG)

These enhancements will build upon the modular architecture established in Version 0.1.
