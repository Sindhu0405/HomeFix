from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
import random
from datetime import datetime, timedelta


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


# ==========================================
# TEMPORARY OTP STORAGE
# ==========================================

otp_storage = {}


# ==========================================
# REQUEST MODEL
# ==========================================

class SendOTPRequest(BaseModel):

    type: str

    email: str | None = None

    mobile: str | None = None

    country_code: str | None = None


class VerifyOTPRequest(BaseModel):

    type: str

    email: str | None = None

    mobile: str | None = None

    country_code: str | None = None

    otp: str


# ==========================================
# SEND OTP
# ==========================================

@router.post("/send-otp")
def send_otp(data: SendOTPRequest):

    # --------------------------------------
    # EMAIL
    # --------------------------------------

    if data.type == "email":

        if not data.email:

            raise HTTPException(
                status_code=400,
                detail="Email is required."
            )

        destination = data.email


    # --------------------------------------
    # MOBILE
    # --------------------------------------

    elif data.type == "mobile":

        if not data.mobile:

            raise HTTPException(
                status_code=400,
                detail="Mobile number is required."
            )

        if not data.country_code:

            raise HTTPException(
                status_code=400,
                detail="Country code is required."
            )

        # India validation

        if data.country_code == "+91":

            if len(data.mobile) != 10:

                raise HTTPException(
                    status_code=400,
                    detail="Indian mobile number must contain 10 digits."
                )

        destination = (
            data.country_code +
            data.mobile
        )


    else:

        raise HTTPException(
            status_code=400,
            detail="Invalid login type."
        )


    # ======================================
    # GENERATE OTP
    # ======================================

    otp = str(
        random.randint(100000, 999999)
    )


    # ======================================
    # OTP EXPIRY
    # ======================================

    expires_at = (
        datetime.utcnow()
        + timedelta(minutes=5)
    )


    # ======================================
    # SAVE OTP
    # ======================================

    otp_storage[destination] = {

        "otp": otp,

        "expires_at": expires_at

    }


    # ======================================
    # DEMO OUTPUT
    # ======================================

    print("")
    print("======================================")
    print("        HOMEFIX OTP")
    print("======================================")
    print("Destination:", destination)
    print("OTP:", otp)
    print("Expires in: 5 minutes")
    print("======================================")
    print("")


    return {

        "success": True,

        "message": "OTP generated successfully."

    }


# ==========================================
# VERIFY OTP
# ==========================================

@router.post("/verify-otp")
def verify_otp(data: VerifyOTPRequest):

    # --------------------------------------
    # FIND DESTINATION
    # --------------------------------------

    if data.type == "email":

        if not data.email:

            raise HTTPException(
                status_code=400,
                detail="Email is required."
            )

        destination = data.email


    elif data.type == "mobile":

        if not data.mobile:

            raise HTTPException(
                status_code=400,
                detail="Mobile number is required."
            )

        if not data.country_code:

            raise HTTPException(
                status_code=400,
                detail="Country code is required."
            )

        destination = (
            data.country_code +
            data.mobile
        )


    else:

        raise HTTPException(
            status_code=400,
            detail="Invalid login type."
        )


    # ======================================
    # CHECK OTP EXISTS
    # ======================================

    saved_otp = otp_storage.get(destination)


    if not saved_otp:

        raise HTTPException(
            status_code=400,
            detail="OTP not found. Please request a new OTP."
        )


    # ======================================
    # CHECK EXPIRY
    # ======================================

    if datetime.utcnow() > saved_otp["expires_at"]:

        del otp_storage[destination]

        raise HTTPException(
            status_code=400,
            detail="OTP expired. Please request a new OTP."
        )


    # ======================================
    # CHECK OTP
    # ======================================

    if data.otp != saved_otp["otp"]:

        raise HTTPException(
            status_code=400,
            detail="Invalid OTP. Please try again."
        )


    # ======================================
    # OTP SUCCESS
    # ======================================

    del otp_storage[destination]


    return {

        "success": True,

        "message": "Login successful."

    }