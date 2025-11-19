from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Jaimy by Belfius Lead Gen API")

# CORS for frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LeadRequest(BaseModel):
    name: str
    email: str
    phone: str
    language: str
    category: str
    details: str | None = None


@app.get("/")
async def root():
    return {"message": "Backend is running", "service": "lead-gen"}


@app.post("/lead")
async def create_lead(lead: LeadRequest):
    # In a real app we'd persist to DB or forward to CRM; here we just echo
    return {"status": "received", "lead": lead.model_dump()}


@app.get("/test")
async def test():
    return {
        "backend": "ok",
        "database": "not-configured",
        "database_url": "",
        "database_name": "",
        "connection_status": "skipped",
        "collections": [],
    }
