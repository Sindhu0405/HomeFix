from fastapi import APIRouter

from ..schemas import DiagnosisRequest, DiagnosisResponse
from ..services.diagnosis import diagnose

router = APIRouter(prefix="/api/diagnosis", tags=["Diagnosis"])


@router.post("", response_model=DiagnosisResponse)
def run_diagnosis(payload: DiagnosisRequest):
    return diagnose(payload.category, payload.symptom)
