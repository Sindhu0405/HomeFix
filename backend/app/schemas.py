from pydantic import BaseModel, ConfigDict


# =========================
# Appliance Schemas
# =========================

class ApplianceCreate(BaseModel):
    name: str
    category: str
    brand: str | None = None
    model: str | None = None
    purchase_year: int | None = None
    warranty_until: str | None = None
    notes: str | None = None


class ApplianceOut(ApplianceCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# Diagnosis Schemas
# =========================

class DiagnosisRequest(BaseModel):
    category: str
    symptom: str


class DiagnosisResponse(BaseModel):
    category: str
    symptom: str
    possible_causes: list[dict]
    safe_checks: list[str]
    estimated_repair_range: str
    recommendation: str


# =========================
# Authentication Schemas
# =========================

class RegisterRequest(BaseModel):
    name: str
    password: str


class LoginRequest(BaseModel):
    name: str
    password: str


class AuthResponse(BaseModel):
    success: bool
    message: str
    user_id: int | None = None
    name: str | None = None