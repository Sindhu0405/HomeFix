from pydantic import BaseModel, ConfigDict


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
