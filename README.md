# HomeFix — AI Appliance Troubleshooting & Maintenance Platform

A full-stack portfolio project for diagnosing common appliance problems, tracking repairs, warranties, and maintenance.

## Stack
- Frontend: React + Vite (planned in Phase 2)
- Backend: FastAPI + SQLAlchemy
- Database: PostgreSQL (SQLite for local starter)
- AI/NLP: planned in Phase 4
- Auth: JWT planned
- Docker/AWS: planned

## Current starter
The included backend is a clean FastAPI foundation with:
- health endpoint
- appliance CRUD
- diagnosis endpoint using a simple rule-based engine
- SQLAlchemy models
- Pydantic schemas
- SQLite local database

## Run backend
```bash
cd backend
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs

## Roadmap
1. Backend foundation
2. React dashboard
3. Authentication
4. PostgreSQL migration
5. Appliance/warranty/repair modules
6. AI troubleshooting and document/manual analysis
7. Cost-based repair vs replace engine
8. Testing, Docker and AWS deployment
